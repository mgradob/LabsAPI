from django.db import models


class Student(models.Model):
    id_student = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=50)
    last_name_1 = models.CharField(max_length=50)
    last_name_2 = models.CharField(max_length=50)
    id_credential = models.IntegerField(max_length=32, null=True)
    career = models.CharField(max_length=5)
    mail = models.EmailField()


class Category(models.Model):
    id_category = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    #image = models.ImageField()


class Component(models.Model):
    id_component = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    note = models.CharField(max_length=250, null=True)
    total = models.IntegerField()
    available = models.IntegerField()
    id_category_fk = models.ForeignKey('Category')


class DetailCart(models.Model):
    id = models.AutoField(primary_key=True)
    id_student_fk = models.ForeignKey('Student')
    id_component_fk = models.ForeignKey('Component')
    quantity = models.IntegerField()
    checkout = models.BooleanField()
    ready = models.BooleanField()
    date_checkout = models.DateTimeField()


class DetailHistory(models.Model):
    id = models.AutoField(primary_key=True)
    id_student_fk = models.ForeignKey('Student')
    id_component_fk = models.ForeignKey('Component')
    quantity = models.IntegerField()
    date_out = models.DateTimeField()
    date_in = models.DateTimeField()