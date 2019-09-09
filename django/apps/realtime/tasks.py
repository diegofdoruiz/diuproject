import time
import redis
import serial
import json
from django.shortcuts import get_object_or_404
from django.contrib import messages
from celery.task.control import revoke
from celery import task
import pyttsx3 as tts
from diufirstprocjet.celery import app
from celery.app.task import Task
from apps.games import control
from apps.games.models import Game
from apps.topics.models import Topic
from apps.califications.models import Calification
from django.contrib.sessions.models import Session
from django.db.models import Sum
from django.db.models import Count


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

"""
########################## Parte 2 del proyecto ###############################################################
"""

@task(bind=True)
def listenBluetooth(self, game_id):
	# Se instancia el juego o partida
	game = get_object_or_404(Game, pk=game_id)
	print("start task")
	port="/dev/tty.MUISCAS-SPPDev" #This will be different for various devices and on windows it will probably be a COM port.
	bluetooth=serial.Serial(port, 9600)#Start communications with the bluetooth unit
	print("Connected")
	# Juego iniciado
	response_data = {}
	response_data['type'] = "start"
	redis_client.publish(game.channel, json.dumps(response_data))
	bluetooth.flushInput() #This gives the bluetooth a little kick
	self.update_state(state="RUNNING")
	#task = app.AsyncResult(self.request.id)
	while(True):
		input_data=bluetooth.readline()#This reads the incoming data. In this particular example it will be the "Hello from Blue" line
		# Formatear lectura del bluetooth
		pressed = input_data.decode("utf-8")
		response_data = {}
		response_data['type'] = "arduino"
		response_data['to_read'] = "topic"
		response_data['arduino_message'] = pressed
		if pressed != "":
			if int(pressed) == 6: # Repetir tema
				readTopic.delay(game_id=game_id, read_question=False)
			elif int(pressed) == 5: # Repetir pregunta
				readQuestion.delay(game_id=game_id)
			elif int(pressed) >= 7 and int(pressed) <= 10: # Inicar un nuevo tema 7 - 10
				nextTopic.delay(game_id=game_id, topic_card_number=int(pressed))
			elif int(pressed) >= 1 and int(pressed) <= 4: # Evaluar la respuesta 1 - 4
				checkAnswer.delay(game_id, "answer_"+str(int(pressed)))
				pass
			redis_client.publish(self.request.id, json.dumps(response_data))
		time.sleep(1)
	print("Stoped")

@task(bind=True)
def readTopic(self, game_id, read_question):
	# Se instancia el juego o partida
	game = get_object_or_404(Game, pk=game_id)
	topics = game.topics.filter(current=True, completed=False)
	# se verifica que haya un tema corriendo y que no se esté leyendo nada
	if topics and not game.reading_topic and not game.reading_question:
		game.reading_topic = True
		game.save()
		# Enviar el tema al front
		response_data = {}
		response_data['type'] = "topic"
		response_data['message'] = topics[0].info
		redis_client.publish(game.channel, json.dumps(response_data))
		control.readText(topics[0].info)
		game.reading_topic = False
		game.save()
		if read_question:
			readQuestion.delay(game_id=game_id)	

@task(bind=True)
def readQuestion(self, game_id, next_question=False):
	# Se instancia el juego o partida
	game = get_object_or_404(Game, pk=game_id)
	topics = game.topics.filter(current=True, completed=False)
	# se verifica que haya un tema corriendo y que no se esté leyendo nada
	if topics and not game.reading_topic and not game.reading_question:
		topic = topics[0]
		questions = topic.questions.filter(current=True, completed=False)
		if questions:
			game.reading_question = True
			game.save()
			if not next_question:
				control.readText("Pregunta... \n")
			else:
				control.readText("Siguiente Pregunta... \n")
			# Enviar la pregunta al front y leerla
			response_data = {}
			response_data['type'] = "question"
			response_data['message'] = questions[0].statement
			redis_client.publish(game.channel, json.dumps(response_data))
			control.readText(questions[0].statement)
			# Enviar respuesta 1 al front y leerla
			control.readText("Respuesta "+str(1)+"...\n")
			response_data = {}
			response_data['type'] = "answer"
			response_data['answer'] = "answer_1"
			response_data['message'] = questions[0].answer_1
			redis_client.publish(game.channel, json.dumps(response_data))
			control.readText(questions[0].answer_1)
			# Enviar respuesta 2 al front y leerla
			control.readText("Respuesta "+str(2)+"...\n")
			response_data = {}
			response_data['type'] = "answer"
			response_data['answer'] = "answer_2"
			response_data['message'] = questions[0].answer_2
			redis_client.publish(game.channel, json.dumps(response_data))
			control.readText(questions[0].answer_2)
			# Enviar respuesta 3 al front y leerla
			control.readText("Respuesta "+str(3)+"...\n")
			response_data = {}
			response_data['type'] = "answer"
			response_data['answer'] = "answer_3"
			response_data['message'] = questions[0].answer_3
			redis_client.publish(game.channel, json.dumps(response_data))
			control.readText(questions[0].answer_3)
			# Enviar respuesta 4 al front y leerla
			control.readText("Respuesta "+str(4)+"...\n")
			response_data = {}
			response_data['type'] = "answer"
			response_data['answer'] = "answer_4"
			response_data['message'] = questions[0].answer_4
			redis_client.publish(game.channel, json.dumps(response_data))
			control.readText(questions[0].answer_4)
			game.reading_question = False
			game.waiting_answer = True
			game.save()

@task(bind=True)
def checkAnswer(self, game_id, answer):
	# Se instancia el juego o partida
	game = get_object_or_404(Game, pk=game_id)
	if game.waiting_answer:
		# control.checkAnswer(game_id, answer)
		if game.waiting_answer and not game.reading_topic and not game.reading_question:
			topics = game.topics.filter(current=True, completed=False)
			if not topics:
				return False
			topic = topics[0]
			questions = topic.questions.filter(current=True, completed=False)
			if not questions:
				return False
			question = questions[0]
			game.reading_question = True
			game.save()
			if answer == question.correct_answer:
				response_data = {}
				response_data['type'] = "confirmation"
				response_data['answer'] = answer
				response_data['message'] = ""
				redis_client.publish(game.channel, json.dumps(response_data))
				# Guardar nota
				calification = Calification()
				calification.note = 5
				calification.question_id = question.id
				calification.student_id = game.user_id
				calification.game_id = game.id
				calification.save()
				control.readText("La Respuesta es correcta... \n");
			else:
				response_data = {}
				response_data['type'] = "confirmation"
				response_data['answer'] = answer
				response_data['message'] = getattr(question, question.correct_answer)
				redis_client.publish(game.channel, json.dumps(response_data))
				# Guardar nota
				calification = Calification()
				calification.note = 0
				calification.question_id = question.id
				calification.student_id = game.user_id
				calification.game_id = game.id
				calification.save()
				control.readText("Respuesta incorrecta... \n");
				control.readText("La Respuesta correcta es... \n");
				control.readText(getattr(question, question.correct_answer))
			question.current = False
			question.completed = True
			question.save() # Se actualiza la preguna como terminada 
			game.waiting_answer = False
			game.reading_question = False
			game.save()
			nextQuestion.delay(game_id=game_id)
	return

@task(bind=True)
def nextQuestion(self, game_id):
	# Se instancia el juego o partida
	game = get_object_or_404(Game, pk=game_id)

	# Se consulta si hay un tema corriendo y no ha finalizado
	topics = game.topics.filter(current=True, completed=False)

	if topics:
		topic = topics[0]
		# se consulta si aún quedan preguntas de este tema
		questions = topic.questions.filter(current=False, completed=False)
		if questions:
			# limpiar pregunta en el front
			response_data = {}
			response_data['type'] = "reset_question"
			redis_client.publish(game.channel, json.dumps(response_data))
			question = questions[0]
			question.current = True
			question.save()
			readQuestion.delay(game_id=game_id, next_question=True)
		else:
			topic.current = False
			topic.completed = True
			topic.save()
			# Se consulta si hay temas disponibles
			topics = game.topics.filter(current=False, completed=False)
			if topics:
				# limpiar tema en el front
				response_data = {}
				response_data['type'] = "reset_topic"
				redis_client.publish(game.channel, json.dumps(response_data))
				control.readText("Por favor seleccione otro punto del mapa\n")
			else:
				sum_notes = Calification.objects.values('game_id').filter(game_id=game.id).order_by('game_id').annotate(note=Sum('note'))
				total_notes = Calification.objects.values('game_id').filter(game_id=game.id).order_by('game_id').annotate(total=Count('note'))
				note = 0
				if sum_notes and total_notes:
					note = sum_notes[0]["note"]/total_notes[0]["total"]
				# Transmitir finalización
				response_data = {}
				response_data['type'] = "finished"
				redis_client.publish(game.channel, json.dumps(response_data))
				control.readText("..........................................\n")
				control.readText("Actividad finalizada...\n")
				# Transmitir la nota
				response_data = {}
				response_data['type'] = "note"
				response_data['value'] = str(note)
				redis_client.publish(game.channel, json.dumps(response_data))
				control.readText("Su nota es ...............\n")
				control.readText(str(note))

		

@task(bind=True)
def nextTopic(self, game_id, topic_card_number):
	# Se instancia el juego o partida
	game = get_object_or_404(Game, pk=game_id)

	# Se consulta si hay un tema corriendo y no ha finalizado
	topics = game.topics.filter(current=True, completed=False)

    # Sí hay un tema en juego, no se puede cambiar. Se retorna
	if topics:
		return False

    # Se instancia el tema
	topic = Topic.objects.filter(card=topic_card_number)[0]

	question = None

	# Si hay un topic corriendo se busca una pregunta
	if topic:
		if topic.completed:
			control.readText("Ya respondió todo acerca de esta cultura...\n")
			control.readText("Por favor seleccione otra cultura...\n")
			return
		# Se procesa el siguiente tema
		if topic.completed == False:
			game.topics.all().update(current=False)
			game.waiting_topic = False
			game.save()
			topic.current = True
			topic.save()

			# Se toma la pregunta que está corriendo
			question = topic.questions.all()[0]
			if question:
				topic.questions.all().update(current=False)
				question.current = True
				question.save()
			# Se lee el topic
			readTopic.delay(game_id=game_id, read_question=True)

@task(bind=True)
def initGame(self, game_id):
	# Se instancia el juego o partida
	game = get_object_or_404(Game, pk=game_id)

	Calification.objects.filter(game_id=game.id).delete()

	# Se hace un reset de las entidades asociadas
	control.resetGame(game)

	# Se pone como juego actual
	game.current = True
	# Se activa el bluetooth
	task_id = listenBluetooth.delay(game_id=game_id)
	game.arduino_task_id = task_id
	game.waiting_topic = True
	game.save()

@task(bind=True)
def stopGame(self, game_id):
	# Se instancia el juego o partida
	game = get_object_or_404(Game, pk=game_id)
	if game.arduino_task_id != None:
		revoke(game.arduino_task_id, terminate=True)
		game.arduino_task_id = None
	# Juego finalizado
	response_data = {}
	response_data['type'] = "stop"
	redis_client.publish(game.channel, json.dumps(response_data))
	game.current = False
	game.channel = None
	game.save()







