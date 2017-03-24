from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def get_upload_path(instance, filename):
    #print(instance.user.username)
    return './{0}/{1}'.format(instance.user.username, filename)

class FileModel(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    f = models.FileField(upload_to=get_upload_path)
    user = models.ForeignKey(User)
    isfavorite = models.BooleanField(default = False)