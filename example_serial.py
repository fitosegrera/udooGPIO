#!/usr/bin python
import udooGPIO

udoo = udooGPIO.UdooGPIO()

def setup():
	udoo.Serial(9600)
	udoo.pinMode(40, "OUTPUT")
	#doo.digitalRead(40)
	
def loop():
	while True:
		udoo.SerialWrite('1')
		udoo.delay(1)
		udoo.SerialWrite('0')
		udoo.delay(1)
	
if __name__ == "__main__":
	setup()
	loop()
		
