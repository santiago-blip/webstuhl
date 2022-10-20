from rest_framework import serializers
from apps.vacancies.models import (Languages, Areas, Levels, Profession, ProfessionDegree, InternalContacts, InternalRelationsObjetives,
ExternalContacts,ExternalRelationsObjetives)

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