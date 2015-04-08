from rest_framework import viewsets
from LabsIndex.models import Labs, Student, Administrator
from LabsIndex import serializers


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
