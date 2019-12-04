from django.db import models

# Create your models here.
class registration(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.EmailField(blank=True)
    password1 = models.CharField(max_length=24)
    password2 = models.CharField(max_length=24)

def __unicode__(self):
        return self.status

def save(self, *args, **kwargs):
    super(registration, self).save(*args, **kwargs)