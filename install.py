# Ruckus Cloud MSP - Python program to extract from API and update influx database.

# Setup.py - Run this script for initial setup. 
# - Store password in operating system keyring securely. Avoid storing password in text readable format.


# pip install keyring, getpass
import getpass
import keyring
import keyring.util.platform_ as keyring_platform
import inquirer
# pip install influxdb
from influxdb import InfluxDBClient

print(keyring_platform.config_root())
# /home/karthik/.config/python_keyring  # Might be different for you
# C:\Users\kmohanakrish\AppData\Local\Python Keyring - WIN
print("=============== Ruckus Cloud Details ==============")
query = [
  inquirer.List('instance',
                message="Select the Ruckus Cloud Instance:",
                choices=['ruckus.cloud', 'asia.ruckus.cloud', 'eu.ruckus.cloud', 'Manually enter domain name eg. <country_code>.ruckus.cloud'],
            ),
]

cloud_instance = inquirer.prompt(query)
if cloud_instance["instance"] == "Manually enter domain name eg. <country_code>.ruckus.cloud":
    RKS_DOMAIN=input("Enter domain name eg. <country_code>.ruckus.cloud : ")
else:
    RKS_DOMAIN=cloud_instance["instance"]

RKS_USERNAME = input("Enter Ruckus Cloud (Read-only) Username: ")
RKS_PASSWORD = getpass.getpass("Ruckus Cloud Password: ")
keyring.set_password(RKS_DOMAIN, RKS_USERNAME, RKS_PASSWORD)

rks_cred = keyring.get_credential(RKS_DOMAIN, RKS_USERNAME)
if rks_cred.password:
    print(f"Password of username {rks_cred.username} for DOMAIN {RKS_DOMAIN} is set successfully")

print("=============== Influx Details ==============")

INFLUX_HOSTNAME = input("Enter InfluxDB Hostname: ")
INFLUX_USERNAME = input("Enter InfluxDB Username: ")
INFLUX_PASSWORD = getpass.getpass("InfluxDB Password: ")
INFLUX_DATABASE = input("Enter InfluxDB Database: ")
keyring.set_password(INFLUX_HOSTNAME, INFLUX_USERNAME, INFLUX_PASSWORD)

flux_cred = keyring.get_credential(INFLUX_HOSTNAME, INFLUX_USERNAME)
if flux_cred.password:
    print(f"Password of username {flux_cred.username} for Influx host {INFLUX_HOSTNAME} is set successfully")

print("=============== SUCCESS ==============")
print("Now you may configure further details in configure.py")
print("")

# defining the host and port  
db_creation = InfluxDBClient(  
    host = INFLUX_HOSTNAME,  
    port = 8086,  
    username = INFLUX_USERNAME,  
    password = INFLUX_PASSWORD,
    )

db_creation.create_database(INFLUX_DATABASE)

#EOL