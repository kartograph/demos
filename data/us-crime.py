import json

cities = json.loads(open('us-cities.json').read())
citiesByName = {}
for city in cities:
	citiesByName[city[0].lower().strip()] = city

crime = json.loads(open('us-crime.json').read())

l = {}
l['portsmouth'] = (43.071396,-70.76643)
l['ventura'] = (34.273957,-119.22987)
l['boulder'] = (40.014994,-105.26453)
l['pompano beach'] = (26.234918,-80.125036)
l['port st. lucie'] = (27.2729, -80.362)
l['st. petersburg'] = (27.773481,-82.640934)
l['west palm beach'] = (26.713107,-80.05537)
l['athens-clarke county'] = (33.952474,-83.382912)
l['st. paul'] = (44.95338,-93.113308)
l['st. louis'] = (38.62599,-90.196781)
l['amherst town'] = (42.366408,-72.517033)
l['charlotte-mecklenburg'] = (35.224307,-80.84095)
l['lewisville'] = (33.045508,-96.994915)
l['odessa'] = (31.844607,-102.367229)
l['richardson'] = (32.946454,-96.729326)
l['round rock'] = (30.506371,-97.678442)
l['tyler'] = (32.349222,-95.300617)
l['west valley'] = (40.697299,-111.994858)


for e in crime:
	name = e["City"].lower().strip()
	if name in citiesByName:
		lon = citiesByName[name][1]
		lat = citiesByName[name][2]
	elif name in l and len(l[name]) == 2:
		lat,lon = l[name]
	else:
		print "missing", name, e["State"]
		
	e["ll"] = (lon,lat)
	

open('us-crime2.json','w').write(json.dumps(crime))
		
	#print e["City"], e["State"]
