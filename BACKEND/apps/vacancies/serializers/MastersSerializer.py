from rest_framework import serializers
from apps.vacancies.models import (Languages, Areas, Levels, Profession, ProfessionDegree, InternalContacts, InternalRelationsObjetives,LevelsAreas,
ExternalContacts,ExternalRelationsObjetives, LanguagesLevels,LanguagesLanguagesLevels)


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

class LanguagesLevelsSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="master-language-level-id",read_only=True)
    class Meta:
        model = LanguagesLevels
        fields = ('id','language_level','url')
class ListLanguagesLevelsFromLanguageSerializer(serializers.ModelSerializer):
    language_level = LanguagesLevelsSerializer(source='language_level_id')
    class Meta:
        model = LanguagesLanguagesLevels
        fields = '__all__'

# class LanguagesSerializer(serializers.HyperlinkedModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="master-language-id",read_only=True)
#     class Meta:
#         model = Languages
#         fields = ('id','language_name','url')
class LanguagesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="master-language-id",read_only=True)
    levels = ListLanguagesLevelsFromLanguageSerializer(source="languageslanguageslevels_set",many = True,read_only=True)
    class Meta:
        model = Languages
        fields = ('id','language_name','url','levels')
        
class LanguagesLanguagesLevelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguagesLanguagesLevels
        fields = '__all__'

class LanguagesLanguagesLevelsListSerializer(serializers.ModelSerializer):
    language_id = LanguagesSerializer()
    language_level_id = LanguagesLevelsSerializer()
    class Meta:
        model = LanguagesLanguagesLevels
        fields = ('id','language_id','language_level_id')

class AreasSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='masterAreaId',
        read_only=True
    )
    class Meta:
        model = Areas
        fields = ('id','area_name','area_description','url')#'__all__'

class LevelsSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='masterLevelId',
        read_only=True
    )
    class Meta:
        model = Levels
        fields = ('id','level_name','level_description','url')

class LevelsAreasSerializer(serializers.ModelSerializer):
    class Meta:
        model = LevelsAreas
        fields = '__all__'

class LevelsDetailsAreasSerializer(DynamicFieldsModelSerializer):
    area_id = AreasSerializer()
    class Meta:
        model = LevelsAreas
        fields = '__all__'

class AreasFromLevelsSerializer(serializers.HyperlinkedModelSerializer):
    areas = LevelsDetailsAreasSerializer(source='levelsareas_set',many = True,fields=('area_id',))
    url = serializers.HyperlinkedIdentityField(
        view_name='masterLevelId',
        read_only=True
    )
    class Meta:
        model = Levels
        fields = ('id','level_name','level_description','url','areas')
class ProfessionSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='masterProfessionId',
        read_only=True
    )
    class Meta:
        model = Profession
        fields = ('id','profession_name','url')
        
class ProfessionDegreeSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='masterProfessionDegreeId',
        read_only=True
    )
    class Meta:
        model = ProfessionDegree
        fields = ('id','profession_degree_name','url')

class InternalContactsSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='master-internal-contact-id',
        read_only=True
    )
    class Meta:
        model = InternalContacts
        fields = ('id','internal_contacts_name','url')

class InternalRelationsObjetivesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='master-internal-relations-objetives-id',
        read_only=True
    )
    class Meta:
        model = InternalRelationsObjetives
        fields = ('id','Internal_relations_objetives_name','url')

class ExternalContactsSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='master-external-contacts-id',
        read_only=True
    )
    class Meta:
        model = ExternalContacts
        fields = ('id','External_contacts_name','url')

class ExternalRelationsObjetivesSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='master-external-relations-objetives-id',
        read_only=True
    )
    class Meta:
        model = ExternalRelationsObjetives
        fields = ('id','External_relations_objetives_name','url')