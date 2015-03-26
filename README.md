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
For more information about udoo's GPIOs layout check: [LINK](http://udoo.org/download/files/pinout/Udoo_pinout_diagram.pdf)

4. run the example script:

		python example.py

__IMPORTANT NOTE:__ Make sure your arduino chip in the udoo has no code uploaded. You might wat to upload an empty scketch to it using the arduinoIDE

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

4. Serial:

		Serial(BAUD)

BAUD: Baudrate for serial interfacing (ei. 9600, 11500, etc...)

5. SerialWrite:

		SerialWrite(DATA)

DATA: Data to write (Recomended char or byte)

__IMPORTANT NOTE:__ In order to use the serial functions of the library you will need to upload a basic code to your arduino chip
then run the "example-serial.py" contained in the folder:

		int led = 12;
		char inChar;

		void setup() {
		  pinMode(led, OUTPUT);
		  digitalWrite(led, LOW);
		  Serial.begin(9600);
		  delay(100);
		  Serial.println("start");
		}

		void loop() {
		  
		  inChar = '\0';
		  while (Serial.available()) {
			inChar = (char)Serial.read();
			if (inChar == '1') { // compare received data
			  digitalWrite(led, HIGH); // turn on light
			  Serial.write(inChar);
			} else{
			  digitalWrite(led, LOW);  // turn off light
			  Serial.write(inChar;
			}
		  }
		  delay(10); 
		}
