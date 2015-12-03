from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class Labs(models.Model):
    name = models.CharField(max_length=100, primary_key=True)
    link = models.URLField(max_length=500)
    #image = models.ImageField()

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

class StudentManager(BaseUserManager):
    def create_user(self, id_student,
                    password):
        user = self.model(id_student=id_student,)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, id_student,
                         password):
        user = self.create_user(id_student,
                                password=password)
        user.is_team_player = True
        user.save()
        return user

class Student(AbstractBaseUser):
    id_student = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    last_name_1 = models.CharField(max_length=50)
    last_name_2 = models.CharField(max_length=50)
    id_credential = models.IntegerField(null=True)
    career = models.CharField(max_length=5)
    mail = models.EmailField()
    labs = models.ManyToManyField(Labs)
    USERNAME_FIELD = 'id_student'

    REQUIRED_FIELDS = ['name', 'last_name_1', 'id_credential', 'career', 'mail']

    objects = StudentManager()
    def __unicode__(self):
        return self.id_student

    class Meta:
        app_label = 'LabsIndex'
        db_table = 'Student'

class AdministratorManager(BaseUserManager):
    def create_admin(self, id_administrator,
                    password=None):
        administrator = self.model(id_administrator=id_administrator,)
        return administrator

    def create_superuser(self, id_administrator,
                         password):
        administrator = self.create_admin(id_administrator,
                                password=password)
        administrator.is_team_player = True
        administrator.save()
        return administrator

class Administrator(AbstractBaseUser):
    id_administrator = models.CharField(max_length=10, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    last_name_1 = models.CharField(max_length=50)
    last_name_2 = models.CharField(max_length=50)
    mail = models.EmailField()
    labs = models.ManyToManyField(Labs)

    USERNAME_FIELD = 'id_administrator'

    REQUIRED_FIELDS = ['name', 'last_name_1', 'last_name_2', 'mail']
    
    objects = AdministratorManager()
    def __unicode__(self):
        return self.id_administrator
