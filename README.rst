Ruckus MSP Cloud monitoring with Grafana
========================================

This project is to pull data from Ruckus Cloud API and store in influxDB.

Grafana helps solving the MSP related problem where an MSP admin can do the following.
1.	Single Dashboard to view all device status irrespective of tenant. 
2.	View limited monitoring information quickly about a tenant without must go to MSP inventory page.
3.	Kiosk requirement – MSP admins often require Kiosk screen to show in a centralized NOC display, which allows quick glance of status of devices. Change settings token_rotation_interval_minutes and login_maximum_inactive_lifetime_days in Grafana.ini 

System Design

Grafana, an open-source tool is implemented as a separate system in a Linux machine. This is only a visualization tool, so it would need a time series database (TSDB) to visualize. In this guide dog we will use Influxdb as the TSDB.
To get the data from Ruckus MSP Cloud to Influxdb, Python program will be used. Python will retrieve data using Ruckus MSP API and moderate it before inserting into Influxdb. 

![System Design](https://github.com/indhradhanush/rkscldmsp_grafana/blob/main/docs/sysdes.PNG?raw=true)
`System Design <https://github.com/indhradhanush/rkscldmsp_grafana/blob/main/docs/sysdes.PNG?raw=true>`_.

`Learn more <https://ruckus.cloud>`_.

---------------
