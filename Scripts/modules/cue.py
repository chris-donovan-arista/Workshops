#TODO: need to move the cue server to the tokenFile
from modules import config
import requests, json

class CueClient():
    def configure():
        config.parser.add_argument('-cueCleanup', default=False, action='store_true', help='do cue cleanup steps')

    def __init__(self, token):
        self.token = token
        self.cookies = None
        self._connected = False

        self._authenticate()

        if not self._connected:
            raise Exception("authentication to cue failed")

    def _authenticate(self) -> bool:
        result = True

        authData = {
            "type": "apiKeyCredentials",
            "keyId": self.token["cue"]["keyid"],
            "keyValue": self.token["cue"]["key"],
            "timeout": 3600,
        }
        url = f'https://launchpad.wifi.arista.com/api/v2/session'
        resp = requests.post(url, json=authData)
        try:
            resp.raise_for_status()
        except:
            return

        authCookies = resp.cookies
        url = f'https://launchpad.wifi.arista.com/api/v2/services?type=amc'
        resp = requests.get(url, cookies=authCookies)
        try:
            resp.raise_for_status()
        except:
            return

        # probably not the safest here...
        wmData = resp.json()["data"]["customerServices"][0]["service"]["service_url"]
        self.baseURL = f'{wmData}/wifi/api/'

        if self.baseURL != self.token["cue"]["url"]:
            raise Exception(f'the computed url of {self.baseURL} does not match the provided token of {self.token["cue"]["url"]}')

        # now let's auth to the amc
        url = f'{self.baseURL}session'
        resp = requests.post(url, json=authData)
        try:
            resp.raise_for_status()
        except:
            return

        self.cookies = resp.cookies
        self._connected = True

    def _doReq(self, reqType: str = 'GET', subsystem: str = None, params=None, data=None) -> dict():
        if not self._connected:
            return

        url = f'{self.baseURL}{subsystem}'

        resp = requests.request(reqType, url=url, params=params, json=data, cookies=self.cookies)
        resp.raise_for_status()
        if reqType in ['GET']:
            return resp.json()

        return {}

    def _doDeleteEvents(self):
        print(f"{config.currentPod} - cue/deleteEvents")
        self._doReq(reqType='DELETE', subsystem='events/bulkdelete')

    def _doDeleteLocations(self):
        print(f"{config.currentPod} - cue/deleteLocations")
        locations = self._doReq(reqType='GET', subsystem='locations')
        for location in locations.get("children", []):
            if location["id"]["id"] > 0:
                data = location["id"]
                self._doReq(reqType='DELETE', subsystem='locations', data=data)

    def _doDeleteRogueAPs(self):
        print(f"{config.currentPod} - cue/deleteRogue")
        self._doReq(reqType='DELETE', subsystem='aps/inactiveauthorized')

    def _doRenameAPs(self):
        print(f"{config.currentPod} - cue/renameAPs")
        aps = self._doReq(reqType='GET', subsystem='manageddevices/aps')
        for ap in aps.get("managedDevices", []):
            data = {
                "name": f'Arista_{ap["macaddress"][-8:]}',
            }
            params = {
                "fields": [ "name" ],
            }
            self._doReq(reqType='PUT', subsystem=f'manageddevices/aps/{ap["macaddress"]}', params=params, data=data)

    def execute(self):
        if config.args.cueCleanup:
            self.cleanup()

    def test(self):
        #r = self._doReq(reqType='GET', subsystem='locations')
        #print(json.dumps(r))
        #return
        params = {
            "locationid": 13,
        }

        r = self._doReq(reqType='GET', subsystem='deviceconfiguration/devicetemplates', params=params)
        print(json.dumps(r))
        pass

    def _doCreateLocations(self):
        with open('files/cue/locations.json', 'r') as f:
            locations = json.load(f)
            self._doReq(reqType='POST', subsystem='locations', data=locations)
        return

    def _doDeleteSSIDs(self, doDelete=True):
        def _doLocationCache(l):
            locationCache[l["id"]["id"]] = l["name"]
            for child in l.get("children", []):
                _doLocationCache(child)

        locationCache = {}
        _doLocationCache(self._doReq(reqType='GET', subsystem='locations'))

        params = {
                "fetchSubTreeTemplates": True
        }

        ssidProfiles = self._doReq(reqType='GET', subsystem='/deviceconfiguration/ssidprofiles', params=params)
        for profile in ssidProfiles:
            print(f'{config.currentPod}/{locationCache[profile["createdAtLocationId"]["id"]]} - {profile["templateName"]}')
            p = {
                "templateid": profile["templateId"],
                "deleteusedssidprofile": True
            }

            if doDelete:
                self._doReq(reqType='DELETE', subsystem=f'deviceconfiguration/ssidprofiles/{profile["templateId"]}', params=p)

    def cleanup(self):
        self._doDeleteEvents()
        self._doDeleteLocations()
        self._doDeleteRogueAPs()
        self._doRenameAPs()
        self._doDeleteSSIDs()

        return
