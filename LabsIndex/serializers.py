__author__ = 'miguel'

from LabsIndex.models import Labs, Student, Administrator
from rest_framework import serializers


class LabsSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedRelatedField(many=True, view_name ='labs-detail', queryset =Labs.objects.all())
    class Meta:
        model = Labs
        fields = ('name', 'link')

class StudentSerializer(serializers.ModelSerializer):
    labs = serializers.HyperlinkedRelatedField(many=True, view_name='labs-detail', queryset=Labs.objects.all())
    password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = Student
        fields = ('id_student', 'name', 'last_name_1',
                  'last_name_2', 'id_credential', 'career', 'mail', 'labs', 'password')

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        labs_data = validated_data.pop('labs', [])
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        for lab_data in labs_data:
            lab_add = Labs.objects.filter(name=lab_data.name)
            instance.labs.add(lab_add)
        return instance

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance

class AdministratorSerializer(serializers.HyperlinkedModelSerializer):
    labs = serializers.HyperlinkedRelatedField(many=True, view_name='labs-detail', queryset=Labs.objects.all())

    class Meta:
        model = Administrator
        fields = ('url', 'id_administrator', 'name', 'last_name_1',
                  'last_name_2', 'mail', 'labs')
