__author__ = 'miguel'

from BetaTesters.models import Tester
from rest_framework import serializers


class TesterSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Tester
        fields = ('url', 'name', 'id_tester')