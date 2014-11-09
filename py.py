import glob
import os

def addCord(a,b):
	print "new google.maps.LatLng(" + a + "," + b + "),"

content = []

# for filename in glob.glob(os.path.join('files2', '*.gpx')):
	# with open(filename) as f:
		# content = f.read().splitlines()

for filename in glob.glob(os.path.join('files2', '*.gpx')):
	with open(filename) as f:
		for line in f:
			if "lat" in line:
				addCord( line[15:25], line[32:42] )

# for item in content:
	# if "lat" in item:
		# print item
	



