# Getting everything set up
1. ### Set up the Pi
..* Plug in the micro-usb to the Pi for power
..* Plug in the display
..* Connect the mouse and keyboard to the Pi
..* Connect the wifi dongle that is in the Pi's case
..* Connect the Pi to the display with the HDMI cable

2. ### Running the code
The code can be found in the "cooling-system" folder on the desktop of the Pi. 

There are two files which have code for the cooling system. The first is "test.py" which simply sets the output pin #15 to high continuously. You can use this for testing if power is being sent. 

The second file is "batteryManagement.py" which runs on output pin #18 and uses simulated data to control the fans based on the average temperature. You can run this to test if the fans turn on and off in response to the changing battery temperatures. 
