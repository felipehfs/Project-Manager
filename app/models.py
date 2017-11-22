from django.db import models

# Create your models here.
class Company(models.Model):
	"""
	Company model
	"""
	name = models.CharField(max_length=40)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name

class Job(models.Model):
	""" """
	name = models.CharField(max_length=50)
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.name
		