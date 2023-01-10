# Ruckus Cloud MSP - Python program to extract from API and update influx database.

# countdata.py - Count AP categories and Customers.
# - Get AP categories based of AP status value from API and return back to called function. Get a list customers. 

from configure import *
from influxapi import *
from collections import Counter

disconnectedcount = 0

def getapcategories(r2):
    c = Counter(player['deviceStatus'] for player in r2)
    c = dict(c)
    return(c)

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