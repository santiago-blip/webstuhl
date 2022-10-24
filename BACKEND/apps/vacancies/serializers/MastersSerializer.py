from rest_framework import serializers
from apps.vacancies.models import (Languages, Areas, Levels, Profession, ProfessionDegree, InternalContacts, InternalRelationsObjetives,LevelsAreas,
ExternalContacts,ExternalRelationsObjetives)


#Permitir seleccionar los fields en serializadores:
class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):

        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)


class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'

class AreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Areas
        fields = '__all__'

class LevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Levels
        fields = '__all__'

class LevelsAreasSerializer(DynamicFieldsModelSerializer):
    area_id = AreasSerializer()
    class Meta:
        model = LevelsAreas
        fields = '__all__'

class AreasFromLevelsSerializer(serializers.ModelSerializer):
    areas = LevelsAreasSerializer(source='levelsareas_set',many = True,fields=('area_id',))
    class Meta:
        model = Levels
        fields = '__all__'
class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profession
        fields = '__all__'
        
class ProfessionDegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionDegree
        fields = '__all__'

class InternalContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalContacts
        fields = '__all__'

class InternalRelationsObjetivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalRelationsObjetives
        fields = '__all__'

class ExternalContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalContacts
        fields = '__all__'

class ExternalRelationsObjetivesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExternalRelationsObjetives
        fields = '__all__'