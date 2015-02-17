__author__ = 'miguel'

from rest_framework import serializers
from Lab_Electronica.models import DetailCart, DetailHistory, Component, Category



class DetailCartSerializer(serializers.HyperlinkedModelSerializer):
    detail_cart = serializers.HyperlinkedRelatedField(many=True, view_name='DetailCart-detail', queryset=DetailCart.objects.all())

    class Meta:
        model = DetailCart
        fields = ('url', 'id_student_fk', 'id_component_fk', 'quantity', 'checkout', 'ready', 'date_checkout')


class DetailHistorySerializer(serializers.HyperlinkedModelSerializer):
    detail_history = serializers.HyperlinkedRelatedField(many=True, view_name='DetailHistory-detail', queryset=DetailHistory.objects.all())

    class Meta:
        model = DetailHistory
        fields = ('url', 'id_student_fk', 'id_component_fk', 'quantity', 'date_out', 'date_in')


class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    component = serializers.HyperlinkedRelatedField(many=True, view_name='Component-detail', queryset=Component.objects.all())

    class Meta:
        model = Component
        fields = ('url', 'id_category_fk', 'id_component', 'name', 'note', 'total', 'available')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(many=True, view_name='Category-detail', queryset=Category.objects.all())

    class Meta:
        model = Category
        fields = ('url', 'id_category', 'name')