from django.db import models

# Create your models here.
class Places(models.Model):
    name=models.CharField(max_length=250)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()

class teams(models.Model):
    name=models.CharField(max_length=200)
    img=models.ImageField(upload_to='pics')
    info=models.TextField()