# Ruckus Cloud MSP - Python program to extract from API and update influx database.

# in_influx_db.py - Store values into influxdb.
# - Store password in operating system keyring securely. Avoid storing password in text readable format.

from configure import *
from influxapi import *
from influx_getaps import *
from influx_getapqty import *
from influx_list import *
from rksapilogin import *
from countdata import *
# pip install requests
import requests

def mspinventory():
    s = requests.Session()
    tenant_id,jw_token = apilogin(s)
    Authorization_Header = {'Authorization': "Bearer {}".format(jw_token)}
    r1 = s.post('https://' + rks_domain + '/api/viewmodel/tenant/' + tenant_id +'/ec-inventory', json={"page": 1,"pageSize": pageSize,"sortField": "deviceStatus","sortOrder": "DESC","matchFields": [{"field": "deviceStatus","value": ""}]}, headers=Authorization_Header).json()
    countinrequest = r1['totalCount']
    print("Total Devices: ",countinrequest)
    if countinrequest > 1:

        #### Temp data for testing Block - START
        y={'serialNumber': 'FJN3851P03E', 'crtTime': '2021-03-08T18:59:03.311Z', 'lastUpdTime': '2021-03-08T18:59:03.311Z', 'name': 'stack-2', 'model': 'ICX7550-24', 'venueId': '1990d21454bb4419a9685f0bf358366b', 'venueName': 'My-Venue', 'deviceStatus': 'ONLINE', 'floorplanId': '', 'xPercent': 0.0, 'yPercent': 0.0, 'tags': '', 'switchName': 'stack-2', 'tenantId': '896ff4566fda421e82ab3e744916c150', 'deviceType': 'DVCNWTYPE_SWITCH', 'switchMac': 'D4:C1:9E:4D:F7:01', 'customerName': 'Bradley Miller', 'managedAs': 'MSP'}
        r1["data"].append(y)
        y={'serialNumber': 'FJN3851P03D', 'crtTime': '2021-03-08T18:59:03.311Z', 'lastUpdTime': '2021-03-08T18:59:03.311Z', 'name': 'stack-1', 'model': 'ICX7150-48ZP', 'venueId': '1990d21454bb4419a9685f0bf358366b', 'venueName': 'My-Venue', 'deviceStatus': 'OFFLINE', 'floorplanId': '', 'xPercent': 0.0, 'yPercent': 0.0, 'tags': '', 'switchName': 'stack-1', 'tenantId': '896ff4566fda421e82ab3e744916c150', 'deviceType': 'DVCNWTYPE_SWITCH', 'switchMac': 'D4:C1:9E:4D:F7:00', 'customerName': 'Bradley Miller', 'managedAs': 'MSP'}
        r1["data"].append(y)
        y={'serialNumber': '46150327824', 'crtTime': '2021-09-04T07:07:31.548Z', 'lastUpdTime': '2021-09-06T11:08:40.700Z', 'lastSeenTime': '2021-11-29T18:38:25.080Z', 'name': 'TestAP1', 'model': 'R500', 'fwVersion': '6.0.0.1.1696', 'venueId': 'a3bcdbb2a90e44089397056a9400c1ba', 'venueName': 'My-Venue', 'configStatus': 'New Configuration', 'connectionStatus': 'Provisioned', 'deviceStatus': '1_01_NeverContactedCloud', 'deviceStatusSeverity': '1_InSetupPhase', 'IP': '192.168.1.111', 'extIp': '124.43.231.104', 'apMac': 'AE:58:EA:23:23:90', 'apStatusData': {'APRadio': [{'txPower': 'max', 'channel': 13, 'band': '2.4G', 'Rssi': None, 'operativeChannelBandwidth': '20', 'radioId': 0}, {'txPower': 'max', 'channel': 36, 'band': '5G', 'Rssi': None, 'operativeChannelBandwidth': '80', 'radioId': 1}], 'APSystem': {'uptime': 709469}, 'lanPortStatus': [{'port': '0', 'phyLink': 'Up 100Mbps full'}, {'port': '1', 'phyLink': 'Down  '}]}, 'meshRole': 'DISABLED', 'deviceGroupId': 'c8d5f0df5fd54a6f82d9d989894005e0', 'floorplanId': '', 'tags': 'D99069', 'deviceGroupName': '', 'deviceModelType': 'Indoor', 'tenantId': '831005cbeb1b48bc9f0b4a20281d9118', 'deviceType': 'DVCNWTYPE_WIFI', 'customerName': 'Bradley Miller', 'managedAs': 'MSP'}
        r1["data"].append(y)
        y={'serialNumber': '34250327824', 'crtTime': '2021-09-04T07:07:31.548Z', 'lastUpdTime': '2021-09-06T11:08:40.700Z', 'lastSeenTime': '2021-11-29T18:38:25.080Z', 'name': 'TestAP2', 'model': 'R510', 'fwVersion': '6.0.0.1.1696', 'venueId': 'a3bcdbb2a90e44089397056a9400c1ba', 'venueName': 'My-Venue', 'configStatus': 'New Configuration', 'connectionStatus': 'Provisioned', 'deviceStatus': '2_00_Operational', 'deviceStatusSeverity': '2_Operational', 'IP': '192.168.1.111', 'extIp': '124.43.231.104', 'apMac': 'AE:58:EA:3A:09:90', 'apStatusData': {'APRadio': [{'txPower': 'max', 'channel': 13, 'band': '2.4G', 'Rssi': None, 'operativeChannelBandwidth': '20', 'radioId': 0}, {'txPower': 'max', 'channel': 36, 'band': '5G', 'Rssi': None, 'operativeChannelBandwidth': '80', 'radioId': 1}], 'APSystem': {'uptime': 709469}, 'lanPortStatus': [{'port': '0', 'phyLink': 'Up 100Mbps full'}, {'port': '1', 'phyLink': 'Down  '}]}, 'meshRole': 'DISABLED', 'deviceGroupId': 'c8d5f0df5fd54a6f82d9d989894005e0', 'floorplanId': '', 'tags': 'D99069', 'deviceGroupName': '', 'deviceModelType': 'Indoor', 'tenantId': '831005cbeb1b48bc9f0b4a20281d9118', 'deviceType': 'DVCNWTYPE_WIFI', 'customerName': 'Bradley Miller', 'managedAs': 'MSP'}
        r1["data"].append(y)
        y={'serialNumber': '84250327824', 'crtTime': '2021-09-04T07:07:31.548Z', 'lastUpdTime': '2021-09-06T11:08:40.700Z', 'lastSeenTime': '2021-11-29T18:38:25.080Z', 'name': 'TestAP3', 'model': 'R550', 'fwVersion': '6.0.0.1.1696', 'venueId': 'a3bcdbb2a90e44089397056a9400c1ba', 'venueName': 'My-Venue', 'configStatus': 'New Configuration', 'connectionStatus': 'Provisioned', 'deviceStatus': '3_04_DisconnectedFromCloud', 'deviceStatusSeverity': '3_RequiresAttention', 'IP': '192.168.1.111', 'extIp': '124.43.231.104', 'apMac': 'AE:58:EA:3A:09:90', 'apStatusData': {'APRadio': [{'txPower': 'max', 'channel': 13, 'band': '2.4G', 'Rssi': None, 'operativeChannelBandwidth': '20', 'radioId': 0}, {'txPower': 'max', 'channel': 36, 'band': '5G', 'Rssi': None, 'operativeChannelBandwidth': '80', 'radioId': 1}], 'APSystem': {'uptime': 709469}, 'lanPortStatus': [{'port': '0', 'phyLink': 'Up 100Mbps full'}, {'port': '1', 'phyLink': 'Down  '}]}, 'meshRole': 'DISABLED', 'deviceGroupId': 'c8d5f0df5fd54a6f82d9d989894005e0', 'floorplanId': '', 'tags': 'D99069', 'deviceGroupName': '', 'deviceModelType': 'Indoor', 'tenantId': '831005cbeb1b48bc9f0b4a20281d9118', 'deviceType': 'DVCNWTYPE_WIFI', 'customerName': 'Bradley Miller', 'managedAs': 'MSP'}
        r1["data"].append(y)
        countinrequest=countinrequest+5
        #### Temp data for testing Block - END
        
        totalcount = min(countinrequest, pageSize)
        r2=r1['data']
        
        statusofaps=getapcategories(r2)
        print(statusofaps)
        
        customers_list=getcustomers(r2)
        print(customers_list)
        in_influx_disconnectedap(statusofaps)

        in_influx_count("customers",getcustomers(r2))
        in_influx_count("venues",getvenues(r2))
        # in_influx_count("models",getmodels(r2))
        
        in_influx_totalap(totalcount)
        in_influx_allap(r1, totalcount)
    else:
        print("No devices found")        
# EOL
