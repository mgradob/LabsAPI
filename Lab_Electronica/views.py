from Lab_Electronica.models import DetailCart, DetailHistory, Component, Category
from rest_framework import viewsets, generics, exceptions
from Lab_Electronica import serializers, permissions
import django_filters


class ComponentFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(name='name', lookup_type='exact')
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
# Create your views here.


class DetailCartViewSet(viewsets.ModelViewSet):
    """
     API endpoint tha allows groups to be viewed or edited.
    """
    queryset = DetailCart.objects.filter(id_student_fk__labs__name='Electronica')
    serializer_class = serializers.DetailCartSerializer
    filter_class = DetailCartFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class DetailHistoryViewSet(viewsets.ModelViewSet):
    """
     API endpoint tha allows groups to be viewed or edited.
    """
    queryset = DetailHistory.objects.filter(id_student_fk__labs__name='Electronica').order_by('id_history')
    serializer_class = serializers.DetailHistorySerializer
    filter_class = DetailHistoryFilter


class ComponentViewSet(viewsets.ReadOnlyModelViewSet):
    """
     API endpoint tha allows groups to be viewed or edited.
    """
    queryset = Component.objects.all()
    serializer_class = serializers.ComponentSerializer
    filter_class = ComponentFilter
    permission_classes = (permissions.IsRegisteredStudentOrReadOnly,)


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """
     API endpoint tha allows groups to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_class = CategoryFilter
    permission_classes = (permissions.IsRegisteredStudentOrReadOnly,)
