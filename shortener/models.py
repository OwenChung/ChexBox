from django.db import models
from unittest.util import _MAX_LENGTH
from .utils import code_generator, create_shortcode
# Create your models here.
class KirrURL(models.Model):
    url = models.CharField(max_length = 220, )
    shortcode = models.CharField(max_length = 15, unique = True, blank = True)
    updated = models.DateTimeField(auto_now = True) # Everytime model is saved
    timestamp = models.DateTimeField(auto_now_add = True) # when model is created
    active = models.BooleanField(default = True)
    # shortcode = models.CharField(max_length = 15, null = True Empty in database is okay)
    # shortcode = models.CharField(max_length = 15, default = 'cfedefdfad')
    
    def save(self, *args, **kargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(KirrURL,self).save(*args, **kargs)
        
    def __str__(self):
        return str(self.url)