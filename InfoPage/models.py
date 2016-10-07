import datetime
from django.db import models

from django.utils import timezone

class student_name(models.Model):
	student_name = models.CharField(max_length=50)
	pub_date = models.DateTimeField('date published')
	spec1 = models.TextField(max_length=500, default="Enter specialization information here.")
	def __str__(self):
		return self.student_name
	def was_updated_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

#class Specialisation(models.Model):
#	student=models.ForeignKey(student_name, on_delete=models.CASCADE, default=0)
#	spec_text = models.CharField(max_length=500)
#	def __str__(self):
#		return self.spec_text

