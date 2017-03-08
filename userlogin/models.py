from django.db import models

# Create your models here.
class FilebabyFile(models.Model):
	"""This holds a single user uploaded file"""
	f = models.FileField(upload_to='.')
	
