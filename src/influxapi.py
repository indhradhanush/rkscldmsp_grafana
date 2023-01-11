# Ruckus Cloud MSP - Python program to extract from API and update influx database.

# influxapi.py - Data to input values into influx.
# - Create a influx client.

from configure import *
# pip install influxdb
from influxdb import InfluxDBClient
# pip install keyring
import keyring

flux_cred = keyring.get_credential(influx_host, influx_username)
influx_password=flux_cred.password

tenant_id = ""

# defining the host and port  
my_Client = InfluxDBClient(  
    host = influx_host,  
    port = influx_port,  
    username = influx_username,  
    password = influx_password,
    )

# creating a database  
# my_Client.create_database(influx_database) 
# setting client to use specified database  
my_Client.switch_database(influx_database) 


