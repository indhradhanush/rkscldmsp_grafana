# Ruckus Cloud MSP - Python program to extract from API and update influx database.

# countdata.py - Count AP categories and Customers.
# - Get AP categories based of AP status value from API and return back to called function. Get a list customers. 

from configure import *
from influxapi import *
from collections import Counter

disconnectedcount = 0

def getapcategories(r2):
    #c = Counter(player['deviceStatus'] for player in r2)
    #c = dict(c)
    dev_status_list = []
    for x in range(0, len(r2)):
        if "deviceStatus" in r2[x]:
            #print("Exists")
            dev_status_list.append(r2[x]['deviceStatus'])
        else:
            #print("Does not exist")
            dev_status_list.append("Unknown")
    print(dev_status_list)
    count_dev = dict(Counter(dev_status_list))
    print(count_dev)
    return(count_dev)

def getcustomers(r2):
    c = Counter(player['customerName'] for player in r2)
    c = dict(c)
    return(c)

def getmodels(r2):
    c = Counter(player['model'] for player in r2)
    c = dict(c)
    return(c)

def getvenues(r2):
    c = Counter(player['venueName'] for player in r2)
    c = dict(c)
    return(c)
