# Ruckus Cloud MSP - Python program to extract from API and update influx database.

# in_influx_getaps.py - get aps from dictionary and store into influx measurement.
# - Analyse and store measurements into measurements in influxdb.

from configure import *
from influxapi import *
from devicestatusmod import *
# pip install influxdb
from influxdb import SeriesHelper

def in_influx_allap(r1,totalcount):
    class MySeriesHelper(SeriesHelper):
        class Meta:
            client = my_Client
            # The series name must be a string. Add dependent fields/tags in curly brackets.
            series_name = rks_domain+"_"+rks_username
            series_name = series_name.replace('@','_')
            series_name = series_name.replace('.','_')
            # series_name = 'allaps'
            # Defines all the fields in this time series.
            fields = ['value']
            # Defines all the tags for the series.
            tags = ['Device_Name', 'Device_type', 'Device_Model', 'Dev_fw', 'Serial_No', 'Device_MAC', 'Device_IPaddr', 'Customer_Name', 'Last_Seen', 'Status', 'Severity', 'ConnectionStatus','ConfigStatus' , 'Uptime', 'Venue_Name']
            # Defines the number of data points to store prior to writing on the wire.
            bulk_size = 500
            # autocommit must be set to True when using bulk_size
            autocommit = True
    counter = 0
    for x in r1['data']:
        counter=counter+1
        print(counter, "out of ----------------", totalcount)
        print(x)
        print('Device Name :',x['name'])
        print('Device Serial No :',x['serialNumber'])
        print('Customer_Name=',x['customerName'])
        print('Venue_Name=',x['venueName'])
        print('Serial_No=',x['serialNumber'])
        #print('Status=',devicestatus_grafana(x['deviceStatus']))

        if x.get('deviceStatus'):
            print('Status=',devicestatus_grafana(x['deviceStatus']))
            device_status=devicestatus_grafana(x['deviceStatus'])
        else:
            device_status="Invalid"
            print('Status=',device_status)

        if x.get('deviceType'):
            if x['deviceType']=='DVCNWTYPE_SWITCH':
                device_type = "Switch"
            elif x['deviceType']=='DVCNWTYPE_WIFI':
                device_type = "Access Point"            
        else:
            device_type="Invalid"
        print('Device_Type=',device_type)

        if x.get('model'):
            device_model=x['model']
            print('Device Model=',x['model'])
        else:
            print('Device Model=Not Found')
            device_model='Not Found'

        if x.get('fwVersion'):
            fw_version=x['fwVersion']
            print('Firmware Version=',x['fwVersion'])
        else:
            print('Firmware Version=Not Found')
            fw_version='Not Found'
        
        if x.get('apMac'):
            devmacaddress=x['apMac']
            if(devmacaddress==x['serialNumber']):
                devmacaddress='00:00:00:00:00'
            print('AP_MAC=',devmacaddress)
        elif x.get('switchMac'):
            devmacaddress=x['switchMac']
            if(devmacaddress==x['serialNumber']):
                devmacaddress='00:00:00:00:00'
            print('AP_MAC=',devmacaddress)
        else:
            print('AP_MAC=00:00:00:00:00')
            apmacaddress='00:00:00:00:00'
        
        if x.get('extIp'):
            print('AP_IPaddr=',x['extIp'])
            devipaddress=x['extIp']
        else:
            print('AP_IPaddr=0.0.0.0')
            devipaddress='0.0.0.0'
        
        if x.get('lastSeenTime'):
            print('Last seen=',x['lastSeenTime'])
            lastseen=x['lastSeenTime']
        else:
            print('Last_Seen=0000-00-00T00:00:00.000Z')
            lastseen='0000-00-00T00:00:00.000Z'
        
        if  x.get('apStatusData', {}).get('APSystem', {}).get('uptime'):
            print('Uptime=',x['apStatusData']['APSystem']['uptime'])
            uptime=x['apStatusData']['APSystem']['uptime']
        else:
            print('uptime=0')
            uptime='0'
        
        if x.get('deviceStatusSeverity'):
            device_severity=deviceseverity_grafana((x['deviceStatusSeverity']))
            print('Severity=',deviceseverity_grafana(x['deviceStatusSeverity']))
        else:
            device_severity="NaN"
            print('Severity=NaN')
        
        if x.get('connectionStatus'):
            print('Connection status=',x['connectionStatus'])
            connection_Status=x['connectionStatus']
        else:
            print('connection_Status=None')
            connection_Status='None'
        
        if x.get('configStatus'):
            print('config status=',x['configStatus'])
            config_Status=x['configStatus']
        else:
            print('config_Status=None')
            config_Status='None'

        MySeriesHelper(Device_Name=x['name'],Device_type=device_type,Device_Model=device_model,Dev_fw=fw_version,Serial_No=x['serialNumber'],Device_MAC=devmacaddress,Device_IPaddr=devipaddress,Customer_Name=x['customerName'],Last_Seen=lastseen,Status=device_status,Severity=device_severity,ConnectionStatus=connection_Status,ConfigStatus=config_Status,Uptime=uptime,Venue_Name=x['venueName'], value=1)
    MySeriesHelper.commit()
    print("Committed to InfluxDB")