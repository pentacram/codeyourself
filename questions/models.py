from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from course.models import *



class Questions(models.Model):
	content = models.ForeignKey(Content, on_delete=models.CASCADE)
	question = models.CharField(max_length=600)	

	def check_answer(self,answer):
		return self.answer_set.filter(id=answer.id, is_answer=True).exists()

	def get_answers(self):
	    return self.answer_set.filter(is_answer=True)

	def __str__(self):
		return self.question

class Answer(models.Model):
	questions = models.ForeignKey(Questions, on_delete=models.CASCADE)
	answer = models.CharField(max_length=600)
	is_answer = models.BooleanField(default=False) 

	def __str__(self):
		return f"{self.questions}, {self.answer}, {self.is_answer}"


