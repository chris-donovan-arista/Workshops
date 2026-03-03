from modules import config
import requests, json, re
#TODO: need to move the url to the token file

class AgniClient():
    def configure():
        config.parser.add_argument('-agniCleanup', default=False, action='store_true', help='do agni cleanup steps')

    def __init__(self, token):
        self.token = token
        self.headers = None
        self._connected = False
        self.baseURL = 'https://beta.agni.arista.io/'

        self._authenticate()

        if not self._connected:
            raise Exception("authentication to agni failed")

    def _authenticate(self):
        authData = {
            "keyID": self.token["agni"]["keyid"],
            "keyValue": self.token["agni"]["key"],
        }

        url = f'{self.baseURL}cvcue/keyLogin'
        resp = requests.get(url, params=authData, verify=False, timeout=300)
        resp.raise_for_status()

        self.headers = {
            "Cookie": resp.json().get("data", {}).get("cookie", None)
        }

        if self.headers["Cookie"]:
            self._connected = True

    def _doReq(self, reqType: str = 'POST', subsystem: str = None, params=None, data={}) -> dict():
        if not self._connected:
            return {}

        data["orgID"] = self.token["agni"]["orgid"]

        url = f'{self.baseURL}api/{subsystem}'

        resp = requests.request(reqType, url=url, params=params, json=data, headers=self.headers)
        resp.raise_for_status()

        try:
            result = resp.json()
            return result
        except requests.exceptions.JSONDecodeError:
            return {}

    def _doDeleteUsers(self):
        print(f"{config.currentPod} - agni/deleteUsers")
        users = self._doReq(subsystem='identity.user.list')

        userPattern = r'^aristaatd(0[0-9]|1[0-9]|20)$'

        for user in users.get("data", {}).get("users", []):
            if not re.match(userPattern, user["loginName"]):
                print(f'  deleting {user["loginName"]}')
                self._doReq(subsystem='identity.user.delete', data=user)

    def _doDeleteClients(self):
        print(f"{config.currentPod} - agni/deleteClients")
        data = {
            "zoneID": 0,
        }
        clients = self._doReq(subsystem='identity.client.list', data=data)

        clientPattern = r'^Pod(0[0-9]|1[0-9]|20)-RaspberryPi$'

        for client in clients.get("data", {}).get("clients", []):
            newClient = self._doReq(subsystem='identity.client.get', data=client)
            #print(json.dumps(newClient, indent=4))

            if "description" in client and not 'raspberrypi' in client["description"].lower():
                print(f'  deleting {client["description"]}')
                self._doReq(subsystem='identity.client.delete', data=client)

    def _doDeleteClientGroups(self):
        print(f"{config.currentPod} - agni/deleteClientGroups")
        clientGroups = self._doReq(subsystem='config.clientGroup.list')

        for clientGroup in clientGroups.get("data", {}).get("clientGroups", []):
            print(f'  deleting {clientGroup["name"]}')
            self._doReq(subsystem='config.clientGroup.delete', data=clientGroup)

    def _doDeleteNetworks(self):
        print(f"{config.currentPod} - agni/deleteNetworks")
        networks = self._doReq(subsystem='config.network.list')

        for network in networks.get("data", {}).get("networks", []):
            print(f'  deleting {network["name"]}')
            self._doReq(subsystem='config.network.delete', data=network)

    def _doDeleteSegments(self):
        print(f"{config.currentPod} - agni/deleteSegments")
        segments = self._doReq(subsystem='config.segment.list')

        for segment in segments.get("data", {}).get("Records", []):
            if segment["name"] == "Default":
                continue

            print(f'  deleting {segment["name"]}')
            self._doReq(subsystem='config.segment.delete', data=segment)

    def _doCreateDefaultSegment(self):
        data = {
            'id': 100000,
            'name': 'Default',
            'description': 'Allow Access',
            'rule': {
                'conditions': [],
                'actions': [
                    {'name': 'Allow Access'}
                ]
            },
            'evalOrder': 100000,
            'isDisabled': False,
            'monitorMode': False,
        }
        self._doReq(subsystem='config.segment.add', data=data)


    def execute(self):
        if config.args.agniCleanup:
            self.cleanup()

    def cleanup(self):
        self._doDeleteUsers()
        self._doDeleteClients()
        self._doDeleteClientGroups()
        self._doDeleteSegments()
        self._doDeleteNetworks()
        return


