import time
import redis
import serial
from django.contrib import messages
from celery.task.control import revoke
from celery import task

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
			if arduino_message != "":
				redis_client.publish(self.request.id, arduino_message)
	except:
		redis_client.publish(self.request.id, "Arduino Desconectado")