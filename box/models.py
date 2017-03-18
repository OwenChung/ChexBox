from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def get_upload_path(instance, filename):
    #print(instance.user.username)
    return './{0}/{1}'.format(instance.user.username, filename)

class FileModel(models.Model):
    f = models.FileField(upload_to=get_upload_path)
    user = models.ForeignKey(User)
