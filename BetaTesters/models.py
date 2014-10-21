from django.db import models


# Create your models here.
class Tester(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    id_tester = models.CharField(max_length=10)