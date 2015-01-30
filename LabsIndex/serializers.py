__author__ = 'miguel'

from LabsIndex.models import Labs, Student
from rest_framework import serializers


class LabsSerializer(serializers.HyperlinkedModelSerializer):
    labs = serializers.RelatedField(many=True)

    class Meta:
        model = Labs
        fields = ('url', 'name', 'link')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.HyperlinkedRelatedField(many=True, view_name='Student-detail')

    class Meta:
        model = Student
        fields = ('url', 'id_student', 'name', 'last_name_1',
                  'last_name_2', 'id_credential', 'career', 'mail', 'labs')
