from Lab_Electronica.models import DetailCart, DetailHistory, Component, Category
from rest_framework import viewsets, generics
from Lab_Electronica import serializers
import django_filters

# Create your views here.


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

#FilterSets

class ComponentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='startswith')
    class Meta:
        model = Component
        fields = ['id_category_fk', 'id_component', 'name', 'note', 'total',
                  'available']

class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='startswith')
    class Meta:
        model = Category
        fields = ['id_category', 'name']

class DetailHistoryFilter(django_filters.FilterSet):

    class Meta:
        model = DetailHistory
        fields = ['id_student_fk', 'id_component_fk', 'quantity', 'date_out',
                  'date_in']

class DetailCartFilter(django_filters.FilterSet):

    class Meta:
        model = DetailCart
        fields = ['id_student_fk', 'id_component_fk', 'quantity', 'checkout',
                  'ready', 'date_checkout']
