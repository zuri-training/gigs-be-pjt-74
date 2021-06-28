from django.db import models

# Create your models here.
class Art(models.Model):
    artname = models.CharField(max_length=150)
    avatar = models.ImageField(upload_to='images/', null=True)
    date = models.DateTimeField(auto_now_add=True)
def __str__(self):
    return self.artname  
     