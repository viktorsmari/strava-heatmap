import glob
import os
import re

b = open('rides.dat', 'w')
b.write('var taxiData =[\n')
x = []

for filename in glob.glob(os.path.join('files/', '*.gpx')):
	with open(filename) as f:
		for line in f:
			if "<trkpt lat" in line:
				x = re.findall('"([^"]*)"', line )
				b.write( "new google.maps.LatLng(" + x[0] + "," + x[1] + "),\n")

b.write(']')
b.close()
