import RPi.GPIO as GPIO
import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
# CLK  = 18
# MISO = 23
# MOSI = 24
# CS   = 25
# mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# LedPin = 11  # pin11

LedPin = 17
PRpin = 0
SSpin = 1

#SETUP
GPIO.setmode(GPIO.BCM)
GPIO.setup(LedPin, GPIO.OUT)
GPIO.setup(PRpin, GPIO.IN)

while True:
	#Test 1 LED Blink
	for k in range(0,5):
		GPIO.output(LedPin, GPIO.HIGH)
		time.sleep(.5)
		GPIO.output(LedPin, GPIO.LOW)
		time.sleep(.5)

	#Photo Resistor Test
	for i in range(50):
		if mcp.read_adc(0) < 550 :
			print("lo ")
		else:
			print("HI")
		# print(GPIO.input(PRpin) )
		time.sleep(.1)

	#Test2 LED Blink
	for j in range(0,5):
		GPIO.output(LedPin, GPIO.HIGH)
		time.sleep(.2)
		GPIO.output(LedPin, GPIO.LOW)
		time.sleep(.2)

	#Sound sensor Test
	for m in range(50):
		if mcp.read_adc(1) > 800 :
			print("LED ON")
			GPIO.output(LedPin, GPIO.HIGH)
			time.sleep(.2)
			GPIO.output(LedPin, GPIO.LOW)
			time.sleep(.1)
		else:
			print(mcp.read_adc(1))
		# print(GPIO.input(PRpin) )
		time.sleep(.1)


#Finished









	
	

