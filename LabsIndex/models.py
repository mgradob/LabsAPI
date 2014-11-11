from django.db import models


# Create your models here.
class Links(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    link = models.URLField(max_length=500)
    #image = models.ImageField()