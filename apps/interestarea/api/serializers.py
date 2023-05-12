
from rest_framework import serializers

from ..models import InterestArea
from apps.subject.models import Subject

class SubjectRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value.uuid)

    def to_internal_value(self, data):
        return Subject.objects.get(uuid=data)

class InterestAreaSerializer(serializers.ModelSerializer): 
    subjects = SubjectRelatedField(
        queryset=Subject.objects.all(),
        many=True
    )
    class Meta:
           model = InterestArea
           fields = ['title', 'slug', 'uuid', 'create_date','subjects']

    def validate_title(self, title: str) -> str:
        # existe uma area de interesse no banco de dados, verifica se esse objeto filtrado é ele se for não
        # não levantar exceção
        if self.instance and InterestArea.objects.filter(title=title).exclude(uuid=self.instance.uuid).exists():
            raise serializers.ValidationError("Já existe uma área de interesse com esse título.")
        elif not self.instance and InterestArea.objects.filter(title=title).exists():
            raise serializers.ValidationError("Esse título já existe.")

        return title  