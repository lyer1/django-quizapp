from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from quizapp.models import Question
import random
import os
import json
from django.db.utils import OperationalError


def start_quiz(request):
    # Initialize session data
    request.session['questions_answered'] = 0
    request.session['correct_answers'] = 0
    request.session['incorrect_answers'] = 0
    request.session['question_ids'] = list(Question.objects.values_list('id', flat=True))
    random.shuffle(request.session['question_ids'])
    return redirect('quiz/')


def quiz(request):

    question_ids = request.session.get('question_ids', [])
    if not question_ids:
        return redirect('end_quiz')

    question_id = question_ids.pop()
    request.session['question_ids'] = question_ids

    question = Question.objects.get(id=question_id)
    return render(request, 'quiz_page.html', {'question': question})


def submit_answer(request):
    if request.method == 'POST':
        question_id = int(request.POST.get('question_id'))
        selected_option = request.POST.get('answer')

        question = Question.objects.get(id=question_id)

        request.session['questions_answered'] += 1

        print(request.POST)

        if selected_option == question.correct_option:
            request.session['correct_answers'] += 1
        else:
            request.session['incorrect_answers'] += 1

        if request.session['question_ids']:
            return redirect('quiz')
        else:
            return redirect('end_quiz')
    if request.method == 'GET':
        print(request.GET)

    return HttpResponse("Invalid request method", status=405)


def end_quiz(request):
    questions_answered = request.session.get('questions_answered', 0)
    correct_answers = request.session.get('correct_answers', 0)
    incorrect_answers = request.session.get('incorrect_answers', 0)

    request.session.flush()

    return render(request, 'quiz_summary.html', {
        'questions_answered': questions_answered,
        'correct_answers': correct_answers,
        'incorrect_answers': incorrect_answers
    })

def ready(request):
    dataset_path = os.path.join(os.path.dirname(__file__), 'questions.jsonl')

    if os.path.exists(dataset_path):
        try:
            if not Question.objects.exists():
                with open(dataset_path, 'r') as file:
                    for line in file:
                        data = json.loads(line)
                        question_data = data['question']
                        Question.objects.create(
                            text=question_data['stem'],
                            option_a=question_data['choices'][0]['text'],
                            option_b=question_data['choices'][1]['text'],
                            option_c=question_data['choices'][2]['text'],
                            option_d=question_data['choices'][3]['text'],
                            option_e=question_data['choices'][4]['text'] if len(question_data['choices']) > 4 else None,
                            correct_option=data.get('answerKey')
                        )
        except OperationalError:
            return HttpResponse("Database error during setup.")
    else:
        return HttpResponse("Questions file not found.")
    return HttpResponse("Questions loaded successfully.")
