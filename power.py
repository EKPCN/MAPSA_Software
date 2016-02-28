from classes import *
import sys, select, os, array
from array import array
from optparse import OptionParser

parser = OptionParser()
parser.add_option('-s', '--setting', metavar='F', type='string', action='store',
default	=	'none',
dest	=	'setting',
help	=	'setting ie on or off')

(options, args) = parser.parse_args()

# create MAPSA object
a = uasic(connection="file://connections_test.xml",device="board0")
mapsa = MAPSA(a)
read = a._hw.getNode("Control").getNode('firm_ver').read()
a._hw.dispatch()
print "Running firmware version " + str(read)

if options.setting=='on':
	print "Voltage on..."

	print "VDDPST on"
	mapsa.VDDPST_on()				
	time.sleep(.5)
	print "DVDD on"
	mapsa.DVDD_on()
	time.sleep(.5)
	print "AVDD on"
	mapsa.AVDD_on()
	time.sleep(.5)
	print "PVDD on"
	mapsa.PVDD_on()

elif options.setting=='off':
	print "Voltage off..."

	print "PVDD off"
	mapsa.PVDD_off()
	print "AVDD off"
	mapsa.AVDD_off()
	print "DVDD off"
	mapsa.DVDD_off()
	print "VDDPST off"
	mapsa.VDDPST_off()
else:
	print "Please select a setting"

print ""
print "Done"
