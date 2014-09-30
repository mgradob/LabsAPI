__author__ = 'miguel'

from rest_framework import serializers
from Lab_Electronica.models import Student, DetailCart, DetailHistory, Component, Category


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ('url', 'id_student', 'name', 'last_name_1', 'last_name_2', 'id_credential', 'career', 'mail')


class DetailCartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetailCart
        fields = ('url', 'id_student_fk', 'id_component_fk', 'quantity', 'checkout', 'ready', 'date_checkout')


class DetailHistorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DetailHistory
        fields = ('url', 'id_student_fk', 'id_component_fk', 'quantity', 'date_out', 'date_in')


class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Component
        fields = ('url', 'id_component', 'name', 'note', 'total', 'available', 'id_category_fk')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'id_category', 'name')