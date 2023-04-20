from django.db import models

# Create your models here.
class Books(models.Model):
    name=models.CharField(max_length=200)
    price=models.TextField()
    year=models.TextField()
    img=models.ImageField(upload_to='pics')
    def __str__(self):
     return self.name