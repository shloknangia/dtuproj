from django.db import models

class student_name(models.Model):
	student_name = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')

class Specialisation(models.Model):
	spec_text = models.CharField(max_length=500)


