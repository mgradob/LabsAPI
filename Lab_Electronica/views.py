from Lab_Electronica.models import Student, DetailCart, DetailHistory, Component, Category
from rest_framework import viewsets
from Lab_Electronica import serializers


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    """
     API endpoint tha allows groups to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = serializers.StudentSerializer


class DetailCartViewSet(viewsets.ModelViewSet):
    """
     API endpoint tha allows groups to be viewed or edited.
    """
    queryset = DetailCart.objects.all()
    serializer_class = serializers.DetailCartSerializer


class DetailHistoryViewSet(viewsets.ModelViewSet):
    """
     API endpoint tha allows groups to be viewed or edited.
    """
    queryset = DetailHistory.objects.all()
    serializer_class = serializers.DetailHistorySerializer


class ComponentViewSet(viewsets.ModelViewSet):
    """
     API endpoint tha allows groups to be viewed or edited.
    """
    queryset = Component.objects.all()
    serializer_class = serializers.ComponentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """
     API endpoint tha allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer