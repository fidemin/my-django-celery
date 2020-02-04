from django.db import models
from django.db.models import Model

class Question(Model):
    index = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, default='')
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'question'


class Choice(Model):
    index = models.AutoField(primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, db_column='question_index')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    class Meta:
        managed=False
        db_table = 'choice'
