__author__ = 'miguel'

from rest_framework import serializers
from Lab_Electronica.models import DetailCart, DetailHistory, Component, Category
from datetime import datetime
from django.utils.timezone import activate, now, localtime

class DetailCartSerializer(serializers.ModelSerializer):
    #detail_cart = serializers.HyperlinkedRelatedField(many=True, view_name='DetailCart-detail', queryset=DetailCart.objects.all())
    #id_cart = serializers.IntegerField()
    def create(self, validated_data):
        cart_data = validated_data.pop('owner')
        cart = DetailCart.objects.create(**validated_data)
        return cart

    class Meta:
        model = DetailCart
        fields = ('id_cart','id_student_fk', 'id_component_fk', 'quantity', 'checkout', 'ready', 'date_checkout',)


class DetailHistorySerializer(serializers.ModelSerializer):
    activate('America/Chihuahua')
    #id_history = serializers.IntegerField()
    #id_student_fk = serializers.StringRelatedField(queryset=DetailHistory.objects.get(id_student_fk__labs__name='Electronica'))
    date_out = serializers.DateTimeField(default=datetime.now)

    class Meta:
        model = DetailHistory
        fields = ('id_history','id_student_fk', 'id_component_fk', 'quantity', 'date_out', 'date_in')

    def to_representation(self, instance):
        activate('America/Chihuahua')
        return {
            'id_history': instance.id_history,
            'id_student_fk': instance.id_student_fk.id_student,
            'id_component_fk': instance.id_component_fk.id_component,
            'quantity': instance.quantity,
            'date_out': localtime(instance.date_out),
            'date_in': instance.date_in
        }

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

