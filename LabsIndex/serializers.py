__author__ = 'miguel'

from LabsIndex.models import Links
from rest_framework import serializers


class LinksSerializer(serializers.HyperlinkedModelSerializer):
    links = serializers.RelatedField(many=True)

    class Meta:
        model = Links
        fields = ('url', 'name', 'link')