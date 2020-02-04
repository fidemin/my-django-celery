from celery import shared_task
from polls.models import Question
import time

@shared_task
def create_question(title, description):
    time.sleep(5)
    question = Question.objects.create(
        title=title,
        description=description)

    return question.pk
