__author__ = 'miguel'

from LabsIndex.models import Links, Student
from rest_framework import serializers


class LinksSerializer(serializers.HyperlinkedModelSerializer):
    links = serializers.RelatedField(many=True)

    class Meta:
        model = Links
        fields = ('url', 'name', 'link')

class StudentSerializer(serializers.HyperlinkedModelSerializer):
    student = serializers.HyperlinkedRelatedField(many=True, view_name='Student-detail')

    class Meta:
        model = Student
        fields = ('url', 'id_student', 'name', 'last_name_1',
                  'last_name_2', 'id_credential', 'career', 'mail', 'labs')
