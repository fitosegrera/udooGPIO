#!/usr/bin python
import sys
import os
import subprocess
import serial
import time

class UdooGPIO:
	
	def __init__(self):
		self.s = None
	
	def pinMode(self, pin, direction):
		self.dirVal = ""
		self.direction = direction
		if self.direction == "INPUT":
			self.dirVal = "in"
		elif self.direction == "OUTPUT":
			self.dirVal = "out"
		else:
			sys.exit("pinMode ERROR: function takes 2 arguments pin# and either INPUT or OUTPUT")
		command = "echo " + self.dirVal + " > /sys/class/gpio/gpio"+str(pin)+"/direction"
		os.system(command)
		
	def digitalWrite(self, pin, value):
		self.state = ""
		if value == "HIGH":
			self.state = "1"
		elif value == "LOW":
			self.state = "0"
		else:
			sys.exit("digitalWrite ERROR: function takes 2 arguments pin# and either HIGH or LOW")
		command = "echo " + self.state + " > /sys/class/gpio/gpio"+str(pin)+"/value"
		os.system(command)
		
	def digitalRead(self, pin):
		self.value = subprocess.check_output(["cat", "/sys/class/gpio/gpio"+str(pin)+"/value"])
		self.data = int(self.value.decode("utf-8"))
		return self.data
	
	def Serial(self, baud):
		self.s = serial.Serial('/dev/ttymxc3', baud, timeout=1)
		self.s.flushOutput()
		
	def SerialWrite(self, data):
		self.s.write(data)
		print data
		
	def delay(self, d):
		time.sleep(d)
