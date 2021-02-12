#!/usr/bin/python

import sys
import time
import Adafruit_DHT

import paho.mqtt.client as mqtt

broker_address="192.168.1.26"
client = mqtt.Client("P1")

sensor = Adafruit_DHT.DHT22
pin = 4

while 1:

     humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

     if humidity is not None and temperature is not None:
    	client.connect(broker_address) #connect to broker
	temp = '{0:0.1f}'.format(temperature)
	hum = '{0:0.1f}'.format(humidity)
    	client.publish("temp",temp)
    	client.publish("hum",hum)
        #print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))
    	time.sleep(5)
     else:
    	print('Failed to get reading. Try again!')
    	sys.exit(1)
