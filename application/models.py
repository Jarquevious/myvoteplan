from django.db import models
from django.db import models


class Question(models.Model):
    question_1 = models.CharField(max_length=200)
    question_2 = models.CharField(max_length=200)
    question_3 = models.CharField(max_length=200)
    question_4 = models.CharField(max_length=200)
    question_5 = models.CharField(max_length=200)
    question_6 = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    def __str__(self):
        return self.choice_text
