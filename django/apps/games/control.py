
from django.shortcuts import get_object_or_404
from apps.games.models import Game
from apps.topics.models import Topic
from apps.questions.models import Question
import pyttsx3 as tts
from google_speech import Speech


def getGame(pk):
	"""
	Obtener el juego en actual.
	"""
	game = get_object_or_404(Game, pk=pk)
	return game

def getTopics(game):
	"""
	Obtener los temas asociados a un juego
	"""
	topics = game.topics.all()
	return topics

def getQuestions(topic):
	"""
	Obtener las preguntas asociadas a un tema
	"""
	questions = topic.questions.all()
	return questions

def resetGame(game):
	"""
	Cambiar el estado del juego y sus entidades asociadas
	"""
	game.completed = False
	game.current = False
	game.waiting_topic = False 
	game.waiting_answer = False
	game.reading_topic = False
	game.reading_question = False
	game.save()

	topics = getTopics(game)
	for topic in topics:
		resetTopic(topic)

def resetTopic(topic):
	"""
	Cambiar el estado del un tema y sus entidades asociadas
	"""
	topic.completed = False
	topic.current = False
	topic.save()

	questions = getQuestions(topic) 
	for question in questions:
		resetQuestion(question)

def resetQuestion(question):
	"""
	Cambiar el estado de una pregunta
	"""
	question.completed = False
	question.current = False
	question.save()

def readText(text):
	"""
	Lee un texto
	"""
	lang = "es"
	speech = Speech(text, lang)
	speech.play()

def test():
	game = getGame(1)
	topics = getTopics(game)
	questions = getQuestions(topics[0])
	resetGame(game)
	readText(topics[0].info)
	print(questions)
