from rest_framework import viewsets
from LabsIndex.models import Links
from LabsIndex import serializers


# Create your views here.
class LinksViewSet(viewsets.ModelViewSet):
    queryset = Links.objects.all()
    serializer_class = serializers.LinksSerializer