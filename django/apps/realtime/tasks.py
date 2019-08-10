import time
import redis
import serial
import json
from django.contrib import messages
from celery.task.control import revoke
from celery import task
import pyttsx3 as tts

# redis_client = redis.StrictRedis(host='redis', port=6379, db=0)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@task(bind=True)
def listenArduino(self):
	arduino_message = ""
	ser = serial.Serial()
	ser.baudrate = 9600
	ser.port = '/dev/cu.usbmodem14101'
	try:
		ser.open()
		while True:
			time.sleep(0.1)
			respuesta = ser.readline()
			arduino_message = respuesta.decode("utf-8")
			response_data = {}
			response_data['type'] = "arduino"
			response_data['to_read'] = "topic"
			response_data['arduino_message'] = arduino_message
			if arduino_message != "":
				redis_client.publish(self.request.id, json.dumps(response_data))
	except:
		response_data = {}
		response_data['type'] = "arduino"
		response_data['arduino_message'] = "Arduino Desconectado"
		redis_client.publish(self.request.id, json.dumps(response_data))

@task(bind=True)
def readText(self, text, key_topic, key_question, to_read):
	engine = tts.init();
	engine.setProperty('rate', 170)
	engine.setProperty('voice', 'spanish')
	engine.say(text)
	engine.runAndWait()
	engine.stop()
	response_data = {}
	response_data['type'] = "reader"
	response_data['key_topic'] = key_topic
	response_data['key_question'] = key_question
	response_data['to_read'] = to_read
	redis_client.publish(self.request.id, json.dumps(response_data))
