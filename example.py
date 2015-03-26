#!/usr/bin python
import udooGPIO

udoo = udooGPIO.UdooGPIO()
pin = 3
def setup():
	udoo.Serial(9600)
	udoo.pinMode(pin, "OUTPUT")
	
def loop():
	while True:
		udoo.digitalWrite(pin, 'HIGH')
		udoo.delay(1)
		udoo.digitalWrite(pin, 'LOW')
		udoo.delay(1)
	
if __name__ == "__main__":
	setup()
	loop()
		
