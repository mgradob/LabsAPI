__author__ = 'miguel'

from rest_framework import serializers
from Lab_Electronica.models import Student, DetailCart, DetailHistory, Component, Category


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.HyperlinkedRelatedField(many=True, view_name='Student-detail')

    class Meta:
        model = Student
        fields = ('url', 'id_student', 'name', 'last_name_1', 'last_name_2', 'id_credential', 'career', 'mail')


class DetailCartSerializer(serializers.HyperlinkedModelSerializer):
    detail_cart = serializers.HyperlinkedRelatedField(many=True, view_name='DetailCart-detail')

    class Meta:
        model = DetailCart
        fields = ('url', 'id_student_fk', 'id_component_fk', 'quantity', 'checkout', 'ready', 'date_checkout')


class DetailHistorySerializer(serializers.HyperlinkedModelSerializer):
    detail_history = serializers.HyperlinkedRelatedField(many=True, view_name='DetailHistory-detail')

    class Meta:
        model = DetailHistory
        fields = ('url', 'id_student_fk', 'id_component_fk', 'quantity', 'date_out', 'date_in')


class ComponentSerializer(serializers.HyperlinkedModelSerializer):
    component = serializers.HyperlinkedRelatedField(many=True, view_name='Component-detail')

    class Meta:
        model = Component
        fields = ('url', 'id_category_fk', 'id_component', 'name', 'note', 'total', 'available')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.HyperlinkedRelatedField(many=True, view_name='Category-detail')

    class Meta:
        model = Category
        fields = ('url', 'id_category', 'name')