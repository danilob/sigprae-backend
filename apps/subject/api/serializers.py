
from rest_framework import serializers

from ..models import Subject

# class UUIDRelatedField(serializers.RelatedField):
#     def to_representation(self, value):
#         return value.uuid

from apps.interestarea.models import InterestArea
class InterestAreaRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value.uuid)

    def to_internal_value(self, data):
        return InterestArea.objects.get(uuid=data)

class SubjectSerializer(serializers.ModelSerializer): 
    interestareas = InterestAreaRelatedField(
        queryset=InterestArea.objects.all(),
        many=True
    )
    class Meta:
        model = Subject
        fields = ['description', 'slug', 'uuid', 'create_date','interestareas']
        extra_kwargs = {'interestareas': {'required': False}}
        
    def validate_description(self, description: str) -> str:
        # existe um objeto no banco de dados, verifica se esse objeto filtrado é ele se for não
        # não levantar exceção
        if self.instance and Subject.objects.filter(description=description).exclude(uuid=self.instance.uuid).exists():
            raise serializers.ValidationError("Essa descrição já existe em outro assunto.")
        elif not self.instance and Subject.objects.filter(description=description).exists():
            raise serializers.ValidationError("Essa descrição já existe.")

        return description
        
class InterestAreaSubjectSerializer(serializers.ModelSerializer): 
    subjects = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = InterestArea
        fields = ['title', 'slug', 'uuid', 'create_date','subjects']
        extra_kwargs = {'subjects': {'required': False}}
    
class SubjectQueriesFilterSerializer(serializers.ModelSerializer):
    interestareas = InterestAreaRelatedField(
        queryset=InterestArea.objects.all(),
        many=True
    )
    class Meta:
        model=Subject
        fields=['description', 'slug', 'uuid', 'create_date','interestareas']
        