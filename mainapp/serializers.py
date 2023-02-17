from rest_framework import serializers
from mainapp.models import (
    School,Teacher,News,Rewiew,Galeria,
)



class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=School
        fields=(
            'id','logo','whatsapp','twitter','facebook','name','description',\
                'admissiontouniversity','staff','students','successworkyear','mail',\
                    'address','number',
                
        )

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=(
            'id','school','name','photo',
        )

class GaleriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Galeria
        fields=(
            'id','school','photo','name',
        )

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=News
        fields = (
            'id', 'description', 'school', 'author',  'created_at',
        )

class RewiewSerializer(serializers.Serializer):
    class Meta:
        model=Rewiew
        fields = (
        'id','photo','parent','description',
        )