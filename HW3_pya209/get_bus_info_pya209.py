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
fout = open(sys.argv[3], "w") 
mode = "Json"
units = "metric"

url = "http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s"%(apikey)

#print (url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
#use the json.loads method to obtain a dictionary representation of the responose string 
dataDict = json.loads(data)


dictkey = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
fout.write("Latitude,Longitude,Stop Name,Stop Distance\n")
for i in dictkey:
	if(i['MonitoredVehicleJourney']['PublishedLineName'] == bus_route):
		lat = i['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
		long = i['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
		if lat == {}:
			lat = "NA"
		if long == {}:
			long = "NA"
		fout.write(str(lat) + ', ' + str(long) + ', ' + str(i['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']) + ', ' + str(i['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']) + '\n')

