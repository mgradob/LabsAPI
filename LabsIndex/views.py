from rest_framework import viewsets, views
from LabsIndex.models import Labs, Student, Administrator
from LabsIndex import serializers
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class LabsViewSet(viewsets.ModelViewSet):
    queryset = Labs.objects.all()
    serializer_class = serializers.LabsSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer

class AdministratorViewSet(viewsets.ModelViewSet):
    queryset = Administrator.objects.all()
    serializer_class = serializers.AdministratorSerializer

