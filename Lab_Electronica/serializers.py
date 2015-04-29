__author__ = 'miguel'

from rest_framework import serializers
from Lab_Electronica.models import DetailCart, DetailHistory, Component, Category



class DetailCartSerializer(serializers.ModelSerializer):
    #detail_cart = serializers.HyperlinkedRelatedField(many=True, view_name='DetailCart-detail', queryset=DetailCart.objects.all())

    class Meta:
        model = DetailCart
        fields = ('id_cart', 'id_student_fk', 'id_component_fk', 'quantity', 'checkout', 'ready', 'date_checkout')


class DetailHistorySerializer(serializers.ModelSerializer):
    #detail_history = serializers.HyperlinkedRelatedField(many=True, view_name='DetailHistory-detail', queryset=DetailHistory.objects.all())

    class Meta:
        model = DetailHistory
<<<<<<< HEAD
        fields = ('id_history','id_student_fk', 'id_component_fk', 'quantity', 'date_out', 'date_in')
=======
        fields = ('id_history', 'id_student_fk', 'id_component_fk', 'quantity', 'date_out', 'date_in')
>>>>>>> parent of 812b2f4... fixed unicode methods and serializers for DetailCart, DetailHistory


class ComponentSerializer(serializers.ModelSerializer):
    #component = serializers.HyperlinkedRelatedField(many=True, view_name='Component-detail', queryset=Component.objects.all())

    class Meta:
        model = Component
        fields = ('id_category_fk', 'id_component', 'name', 'note', 'total', 'available')


class CategorySerializer(serializers.ModelSerializer):
    #category = serializers.HyperlinkedRelatedField(many=True, view_name='Category-detail', queryset=Category.objects.all())

    class Meta:
        model = Category
        fields = ('id_category', 'name')
