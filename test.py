# from django.shortcuts import render
# from django.http import JsonResponse
# from django.db import models
# import random
# import os
# import django

# # Configure settings for standalone script
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz_asgn.settings')
# django.setup()

# # Models
# class Question(models.Model):
#     text = models.CharField(max_length=255)
#     option_a = models.CharField(max_length=100)
#     option_b = models.CharField(max_length=100)
#     option_c = models.CharField(max_length=100)
#     option_d = models.CharField(max_length=100)
#     correct_option = models.CharField(max_length=1, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')])

# class QuizSession(models.Model):
#     questions_answered = models.IntegerField(default=0)
#     correct_answers = models.IntegerField(default=0)
#     incorrect_answers = models.IntegerField(default=0)

# # Views
# def start_quiz(request):
#     session = QuizSession.objects.create()
#     return JsonResponse({'message': 'New quiz session started.', 'session_id': session.id})

# def get_question(request, session_id):
#     session = QuizSession.objects.get(id=session_id)
#     question = random.choice(Question.objects.all())
#     return JsonResponse({
#         'question_id': question.id,
#         'text': question.text,
#         'options': {
#             'A': question.option_a,
#             'B': question.option_b,
#             'C': question.option_c,
#             'D': question.option_d
#         }
#     })

# def submit_answer(request, session_id):
#     session = QuizSession.objects.get(id=session_id)
#     question_id = request.POST.get('question_id')
#     selected_option = request.POST.get('selected_option')

#     question = Question.objects.get(id=question_id)
#     session.questions_answered += 1

#     if selected_option == question.correct_option:
#         session.correct_answers += 1
#         result = 'correct'
#     else:
#         session.incorrect_answers += 1
#         result = 'incorrect'

#     session.save()
#     return JsonResponse({'result': result, 'correct_option': question.correct_option})

# def quiz_summary(request, session_id):
#     session = QuizSession.objects.get(id=session_id)
#     return JsonResponse({
#         'questions_answered': session.questions_answered,
#         'correct_answers': session.correct_answers,
#         'incorrect_answers': session.incorrect_answers
#     })

# # URLs
# from django.urls import path

# urlpatterns = [
#     path('start/', start_quiz, name='start_quiz'),
#     path('question/<int:session_id>/', get_question, name='get_question'),
#     path('submit/<int:session_id>/', submit_answer, name='submit_answer'),
#     path('summary/<int:session_id>/', quiz_summary, name='quiz_summary'),
# ]
