from django.db import models
from LabsIndex.models import Student

class Category(models.Model):
    id_category = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    #image = models.ImageField()

    def __unicode__(self):
        return self.name

class Component(models.Model):
    id_component = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    note = models.CharField(max_length=250, null=True)
    total = models.IntegerField()
    available = models.IntegerField()
    id_category_fk = models.ForeignKey(Category, related_name='category')

    def __unicode__(self):
        return self.name

class DetailCart(models.Model):
    id_student_fk = models.ForeignKey(Student, related_name='student_cart')
    id_component_fk = models.ForeignKey(Component, related_name='component_cart')
    quantity = models.IntegerField()
    checkout = models.BooleanField(default=False)
    ready = models.BooleanField(default=False)
    date_checkout = models.DateTimeField(null=True)
    id_cart = models.AutoField(primary_key=True)

    def __unicode(self):
        return str(self.id_cart)

class DetailHistory(models.Model):
    id_student_fk = models.ForeignKey(Student, related_name='student_history')
    id_component_fk = models.ForeignKey(Component, related_name='component_history')
    quantity = models.IntegerField()
    date_out = models.DateTimeField()
    date_in = models.DateTimeField(null=True)
    id_history = models.AutoField(primary_key=True)

    def __unicode__(self):
        return str(self.id_history)
