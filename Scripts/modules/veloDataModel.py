from modules import config
import json, ipaddress

class veloBaseRoutedInterface():
    def __init__(self, name):
        self.interface = json.loads(
"""
{
  "addressing": {
    "cidrIp": null,
    "cidrPrefix": null,
    "gateway": null,
    "netmask": null,
    "type": "DHCP"
  },
  "advertise": false,
  "disableV4": false,
  "disableV6": true,
  "disabled": false,
  "dnsProxy": false,
  "edgeToEdgeEncryption": true,
  "encryptOverlay": true,
  "evdslModemAttached": false,
  "l2": {
    "MTU": 1500,
    "autonegotiation": true,
    "duplex": "FULL",
    "losDetection": false,
    "probeInterval": "3",
    "speed": "100M"
  },
  "multicast": {
    "igmp": {
      "enabled": false,
      "type": "IGMP_V2"
    },
    "igmpHostQueryIntervalSeconds": null,
    "igmpMaxQueryResponse": null,
    "pim": {
      "enabled": false,
      "type": "PIM_SM"
    },
    "pimHelloTimerSeconds": null,
    "pimKeepAliveTimerSeconds": null,
    "pimPruneIntervalSeconds": null
  },
  "name": "GE1",
  "natDirect": false,
  "ospf": {
    "MTU": 1380,
    "area": "",
    "authId": 0,
    "authPassphrase": "",
    "authentication": false,
    "cost": 1,
    "deadTimer": 40,
    "enableBfd": false,
    "enabled": false,
    "helloTimer": 10,
    "inboundRouteLearning": {
      "defaultAction": "LEARN",
      "filters": []
    },
    "md5Authentication": false,
    "mode": "BCAST",
    "outboundRouteAdvertisement": {
      "defaultAction": "IGNORE",
      "filters": []
    },
    "passive": false
  },
  "overlayPreference": "IPv4",
  "override": true,
  "pingResponse": true,
  "radiusAuthentication": {
    "aclCheck": false,
    "enabled": false,
    "macBypass": []
  },
  "rpf": "SPECIFIC",
  "segmentId": 0,
  "slave": false,
  "trusted": false,
  "underlayAccounting": true,
  "v6Detail": {
    "addressing": {
      "cidrIp": null,
      "cidrPrefix": null,
      "gateway": null,
      "interfaceAddress": null,
      "netmask": null,
      "tag": null,
      "tagLogicalId": null,
      "type": "DHCP_STATELESS"
    },
    "clientPrefixDelegation": {
      "enabled": false,
      "tag": null,
      "tagLogicalId": null
    },
    "natDirect": true,
    "ospf": {
      "MTU": 1380,
      "area": "",
      "cost": 1,
      "deadTimer": 40,
      "enableBfd": false,
      "enabled": false,
      "helloTimer": 10,
      "inboundRouteLearning": {
        "defaultAction": "LEARN",
        "filters": []
      },
      "mode": "BCAST",
      "outboundRouteAdvertisement": {
        "defaultAction": "IGNORE",
        "filters": []
      },
      "passive": false
    },
    "rpf": "SPECIFIC",
    "trusted": false,
    "wanOverlay": "AUTO_DISCOVERED"
  },
  "vlanId": null,
  "wanOverlay": "DISABLED"
}
""")
        self.interface["name"] = name

    def setLagSlave(self):
        self.interface["slave"] = True

    def setLag(self, slaves):
        self.interface["lacp"] = {
            "lacpRate": 0,
            "mode": "Active",
            "sysPriority": 65535
        }

        self.interface["slaveInterfaces"] = slaves

    def setDisabled(self):
        self.interface["disabled"] = True

    def setL3(self, basePrefix):

        net = ipaddress.ip_network(basePrefix)
        netHosts = net.hosts()
        gwAddress = str(next(netHosts))
        firstAddress = 2 #int(str(next(netHosts)).split('.')[3])

        if not basePrefix:
            # we want dhcp
            self.interface["addressing"] = {
                "cidrIp": None,
                "cidrPrefix": None,
                "gateway": None,
                "interfaceAddress": None,
                "netmask": None,
                "tagLogicalId": None,
                "type": "DHCP_STATELESS"
                }
        else:
            self.interface["addressing"] = {
                "cidrIp": gwAddress,
                "cidrPrefix": net.prefixlen,
                "gateway": None,
                "interfaceAddress": None,
                "netmask": str(net.netmask),
                "tagLogicalId": None,
                "type": "STATIC"
                }

            self.interface["advertise"] = True
            self.interface["dhcpServer"] = {
              "baseDhcpAddr": firstAddress,
              "options": [
                {
                  "value": f"http://10.0.96.20:8000/bootstrap.py",
                  "type": "text",
                  "option": 67,
                  "metaData": {
                    "option": 67,
                    "name": "Boot File Name",
                    "description": "Boot file name",
                    "dataType": "text",
                    "list": False,
                    "display": True
                  }
                },
                {
                  "value": [
                    "100.64.0.1"
                  ],
                  "type": "ipv4",
                  "option": 6,
                  "metaData": {
                    "option": 6,
                    "name": "DNS Servers",
                    "description": "List of DNS server addresses",
                    "dataType": "ipv4",
                    "list": True,
                    "display": True
                  }
                }
              ],
              "numDhcpAddr": net.num_addresses-3,
              "enabled": True,
              "leaseTimeSeconds": 900,
              "staticReserved": 10
            }
            self.interface["dnsProxy"] = True
