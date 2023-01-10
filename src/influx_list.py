# Ruckus Cloud MSP - Python program to extract from API and update influx database.

# influx_list.py - Store Customer, Device model names values into influxdb measurements.
# - Get list of customer or Device (AP/ICX Switch) Model names and store into a measurement.

from configure import *
from influxapi import *

def in_influx_count(measurement,count):
    json_body = [ 
        {  
            "measurement": measurement,  
            "tags": count,
            "fields" : {
                "value" : 1
            }
        }  
    ] 
    my_Client.write_points(json_body, time_precision='ms')