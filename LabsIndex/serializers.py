__author__ = 'miguel'

from LabsIndex.models import Labs, Student
from rest_framework import serializers


class LabsSerializer(serializers.HyperlinkedModelSerializer):
    labs = serializers.HyperlinkedRelatedField(many=True, view_name ='labs-detail')
    class Meta:
        model = Labs
        fields = ('url', 'name', 'link')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.HyperlinkedRelatedField(many=True, view_name='student-detail', queryset=Labs.objects.all())

    class Meta:
        model = Student
        fields = ('url', 'id_student', 'name', 'last_name_1',
                  'last_name_2', 'id_credential', 'career', 'mail', 'labs')
