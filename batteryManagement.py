# Libraries
import RPi.GPIO as GPIO
from time import sleep
import random

# Variables
fansOn = False
pastMax = True
maxTemp = 85
safeTemp = maxTemp-10
averageTemp = 0
minRandTemp = 75
randomRange = 15
numBatteries = 24
totalValue = 0
outputPin = 18
tempValues=[]

# Set up GPIO pins
# Output is 3.3 V

# Print out the GPIO mode
mode = GPIO.getmode()
#print mode

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)
GPIO.setup(outputPin,GPIO.OUT)



while True:

	# Generate 24 random values in range from min temp
	totalValue = 0
	for i in range(0, numBatteries):
		randomValue = random.uniform(minRandTemp,minRandTemp+randomRange)
		tempValues.append(float(randomValue))
		totalValue = totalValue + randomValue

	averageTemp = totalValue/numBatteries

	if averageTemp > maxTemp:
		fansOn = True
		pastMax = True
		GPIO.output(outputPin,GPIO.HIGH)
		minRandTemp = minRandTemp-1
		
	elif pastMax == True and averageTemp > safeTemp:
                fansOn = True;
                GPIO.output(outputPin,GPIO.HIGH)
                minRandTemp = minRandTemp-1
	
	else:
		fansOn = False
		pastMax = False
		GPIO.output(outputPin,GPIO.LOW)
		#GPIO.output(outputPin,GPIO.HIGH)
		minRandTemp = minRandTemp+0.5

	# Sleep for one second
	print "average temp = "+"%d" % (averageTemp)
	print "fans on = "+"%r" % (fansOn)
	sleep(1)

# Note that this module is unsuitable for real-time or timing critical applications. This is because you can not predict when Python will be busy garbage collecting. It also runs under the Linux kernel which is not suitable for real time applications - it is multitasking O/S and another process may be given priority over the CPU, causing jitter in your program. If you are after true real-time performance and predictability, buy yourself an Arduino http://www.arduino.cc !

# If GPIO isn't working
# sudo apt-get update
# sudo apt-get -y install python-rpi.gpio

# Website
# https://sourceforge.net/p/raspberry-gpio-python/wiki/BasicUsage/
