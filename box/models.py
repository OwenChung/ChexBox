from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
# Create your models here.

def get_upload_path(instance, filename):
    #print(instance.user.username)
    return './{0}/{1}'.format(instance.user.username, filename)

class FileModel(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    f = models.FileField(upload_to=get_upload_path)
    user = models.ForeignKey(User)
    isfavorite = models.BooleanField(default = False)
#    shared_with = [User.username]
    shared_with = ArrayField(models.CharField(max_length=30),blank=True,null=True)
 
