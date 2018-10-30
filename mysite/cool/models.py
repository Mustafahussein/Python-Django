from django.db import models

# Create your models here.

from django.db import models

class Question(models.Model):
    question_text = models.Charfield(max_length=200)
    pub_date = models.DateTimeField('date published')

    class Choice(models.Model):
        question = models.Foreignkey(Question, on_delete=models.CASCADE)
        choice_text = modles.Charfield(max_length=200)
        votes = models.IntegerField(default=0)