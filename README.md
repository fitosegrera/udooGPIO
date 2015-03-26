# udooGPIO
Python Library with arduino-like syntax to use the GPIOs from the UDOO board. No installation required!!

###Dependencies
1. pyserial - install it with the following terminal command
	sudo pip install pyserial

###Instructions
1. Download or clone the repository
2. Go into the repository folder you just downloaded:
	cd udooGPIO
3. Connect an led with the anode (+) to GPIO 3 (arduino's pin 12) and the cathode (-) to ground
4. run the example script:
	python example.py

IMPORTANT NOTE: Make sure your arduino chip in the udoo has no code uploaded. You might wat to upload an empty scketch to it using the arduinoIDE

###API Reference

1. Declaring pin mode:
	pinMode(PIN, DIRECTION):
PIN: pin number (must be an integer)
DIRECTION: "INPUT" or "OUTPUT" (must be a string)

2. Digital Write:

	digitalWrite(PIN, VALUE)

PIN: pin number (must be an integer)

VALUE: "HIGH" or "LOW" (must be a string)

3. Digital Read:

	digitalRead(PIN)

PIN: pin number (must be an integer)

returns the value read, either 1 or 0