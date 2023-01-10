# Ruckus Cloud MSP - Python program to extract from API and update influx database.

# app.py - Main code file.
# - Call required functions from main.

from mspinventory import *

mspinventory()

#schedule.every(5).minutes.do(mspinventory)

#while True:
#    schedule.run_pending()
#    time.sleep(5)