import time
import redis
import serial
from django.contrib import messages
from celery.task.control import revoke
from celery import task

redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

@task(bind=True)
def listenArduino(self):
	arduino_message = ""
	ser = serial.Serial()
	ser.baudrate = 9600
	ser.port = '/dev/cu.usbmodem14201'
	ser.open()
	while True:
		time.sleep(0.1)
		respuesta = ser.readline()
		arduino_message = respuesta.decode("utf-8")
		if arduino_message != "":
			redis_client.publish(self.request.id, arduino_message)

def stopGame(self, task_id):
	revoke(task_id, terminate=True)

# @task(bind=True)
# def listenArduino(self):
# 	print(self.request.id)
# 	time.sleep(5)
# 	redis_client.publish(self.request.id, 'http://bit.ly/2a2EiIQ')