import RPi.GPIO as GPIO

outputPin = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(True)
GPIO.setup(outputPin,GPIO.OUT)

while (True):
    GPIO.output(outputPin,GPIO.HIGH)