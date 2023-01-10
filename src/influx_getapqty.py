# Ruckus Cloud MSP - Python program to extract from API and update influx database.

# influx_getapqty.py - Get quantities of APs.
# - Get AP quantities and store in measurement.
# - Total AP
# - AP qty based on Status of APs

from configure import *
from influxapi import *

def in_influx_totalap(totalap):
    json_body = [ 
        {  
            "measurement": "totalap",
            "fields": {  
                "totalap": int(totalap)  
            }  
        }  
    ] 
    my_Client.write_points(json_body, time_precision='ms')
    print("Total AP done")

def in_influx_disconnectedap(disconnectedap):
    json_body = [ 
        {  
            "measurement": "downap",  
            "fields": disconnectedap
        }  
    ] 
    my_Client.write_points(json_body, time_precision='ms')
    print("Dis AP done")

#EOL