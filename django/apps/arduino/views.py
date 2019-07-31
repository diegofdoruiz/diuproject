from django.shortcuts import render, redirect, get_object_or_404
import serial
import time
from django.contrib import messages
# Create your views here.

def home(request):
	return render(request, 'home.html', {})

def test(request):
	if request.method == 'POST':
		times = request.POST.get('times', 0)
		respuesta = "No se encenderá el bombillo"
		if int(times) > 0:
			ser = serial.Serial()
			ser.baudrate = 115200
			ser.port = '/dev/cu.usbmodem14201'
			ser.open()
			if(ser.isOpen() == True):
				print('Abierto')
			time.sleep(2)
			send = bytearray()
			send.extend(str(times).encode('latin-1'))
			ser.write(send)
			time.sleep(1)
			respuesta = ser.readline()
			messages.add_message(request, messages.INFO, respuesta.decode("utf-8"), 'respuesta')
			ser.close()
			return redirect('arduino:test')
		return render(request, 'arduino.html', {'respuesta':respuesta})
	else:
		return render(request, 'arduino.html', {})
	