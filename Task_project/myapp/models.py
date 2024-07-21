from django.db import models

# Create your models here.
class Faculty(models.Model):
	fac_name=models.CharField(max_length=100)
	email=models.EmailField()
	password=models.CharField(max_length=100)

	def __str__(self):
		return self.fac_name


class Student(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	s_email=models.EmailField()
	address=models.TextField()
	gender=models.CharField(max_length=100)
	ed_qua=models.CharField(max_length=100)
	password=models.CharField(max_length=100)

	def __str__(self):
		return self.fname+" "+self.lname