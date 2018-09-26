from __future__ import print_function
import json
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys


apikey = sys.argv[1]
bus_route = sys.argv[2]
mode = "Json"
units = "metric"

url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s"%(apikey)

#print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)


count = 0

dictkey = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
print("Bus Line: %s"%(bus_route))

for i in dictkey:
	if(i['MonitoredVehicleJourney']['PublishedLineName'] == bus_route):
		count += 1

print("Number of Active Buses: " + str(count))

count = 0

for i in dictkey:
	if(i['MonitoredVehicleJourney']['PublishedLineName'] == bus_route):
		print("Bus " + str(count) + " is at latitude " + str(i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']) + ' and longitude  ' + str(i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
		count += 1
