from rest_framework import viewsets, permissions
from BetaTesters.models import Tester
import serializers


class TestersViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.AllowAny,)
    queryset = Tester.objects.all()
    serializer_class = serializers.TesterSerializer
