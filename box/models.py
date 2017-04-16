from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import random
import string
# Create your models here.

def get_upload_path(instance, filename):
    #print(instance.user.username)
    #return './{0}/{1}'.format(instance.user.username, filename)
    r = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])

    return './{0}/'.format(instance.user.username)+r+'/{0}'.format(filename)

class FileModel(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    f = models.FileField(upload_to=get_upload_path)
    user = models.ForeignKey(User)
    isfavorite = models.BooleanField(default = False)
#    shared_with = [User.username]
    shared_with = ArrayField(models.CharField(max_length=30),blank=True,null=True)
 
