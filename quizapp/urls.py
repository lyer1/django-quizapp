from django.urls import path
from quizapp.views import *

urlpatterns = [
    path('', start_quiz, name='start_quiz'),
    path('quiz/', quiz, name='quiz'),
    path('submit/', submit_answer, name='submit_answer'),
    path('end_quiz/', end_quiz, name='end_quiz'),
    path('ready/', ready, name='ready'),
]