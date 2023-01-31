from bdb import Breakpoint
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.vacancies.models import (Languages,LanguagesLevels ,Areas, Levels, Profession, ProfessionDegree,InternalContacts,
InternalRelationsObjetives,ExternalContacts,ExternalRelationsObjetives,LevelsAreas,LanguagesLanguagesLevels)

from apps.vacancies.serializers.MastersSerializer import (LanguagesSerializer,AreasSerializer,LevelsSerializer, ProfessionSerializer,LevelsAreasSerializer,
ProfessionDegreeSerializer,LanguagesLanguagesLevelsListSerializer,ListLanguagesLevelsFromLanguageSerializer,
LanguagesLanguagesLevelsSerializer,LanguagesLevelsSerializer,InternalContactsSerializer,InternalRelationsObjetivesSerializer, ExternalContactsSerializer, ExternalRelationsObjetivesSerializer, AreasFromLevelsSerializer)


class LanguagesMasterView(APIView):
    def validate_existing_language_level(self,request,instance,action):
        try:
            levels = request.data.pop('levels') 
            levels = [x.get('id') for x in levels]
        except:
            levels = None
        # breakpoint()
        if levels:
            if action == 'create' :
                sendToLanguagesLevelsRel = [LanguagesLanguagesLevels(language_level_id=LanguagesLevels.objects.filter(id=x).first(),language_id=instance) for x in levels]
                LanguagesLanguagesLevels.objects.bulk_create(sendToLanguagesLevelsRel) 
            else :
                if not request.data.get('toDelete'):
                    existingLevelsIds = LanguagesSerializer(instance,context={'request':request})
                    for x in existingLevelsIds.data.get('levels'):
                        levels.remove(x.get('language_level').get('id'))
                    try:
                        sendToLanguagesLevelsRel = [LanguagesLanguagesLevels(language_level_id=LanguagesLevels.objects.filter(id=x).first(),language_id=instance) for x in levels]
                        LanguagesLanguagesLevels.objects.bulk_create(sendToLanguagesLevelsRel)
                    except:
                        pass
                else:
                    query = LanguagesLanguagesLevels.objects.filter(language_level_id__in=request.data.get('toDelete'),language_id=instance.id)
                    query.delete()
    def get(self,request,pk=None):
        if pk:
            query = Languages.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Lenguaje no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = LanguagesSerializer(query,context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = Languages.objects.all()
        if not query:
            return Response({'error':'No hay lenguajes.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = LanguagesSerializer(query,many = True,context={'request': request})
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = LanguagesSerializer(data=request.data,context={'request': request})
        data.is_valid(raise_exception=True)
        # levelsIds = [x.get('id') for x in request.data.get('levels')]
        # breakpoint()
        # validatedData = LanguagesLanguagesLevels.objects.filter(language_id_language_name__iexact=data.validated_data['language_name'],language_level_id__in=levelsIds)
        # if validatedData:
        #     return Response({'error':'El lenguaje que intenta crear ya existe'},status=status.HTTP_400_BAD_REQUEST)
        instance = data.save()
        self.validate_existing_language_level(request,instance,'create')
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Languages.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = LanguagesSerializer(query,data=request.data,context={'request': request})
        serializedQuery.is_valid(raise_exception=True)
        # validatedData = Languages.objects.filter(language_name__iexact=serializedQuery.validated_data['language_name']).first()
        # if validatedData:
        #     return Response({'error':'El lenguaje que intenta actualizar ya existe'},status=status.HTTP_400_BAD_REQUEST)
        instance= serializedQuery.save()
        self.validate_existing_language_level(request,instance,'update')
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Languages.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        
        query.delete()
        return Response({'response':'Eliminado con éxito.'},status=status.HTTP_200_OK)

class LanguagesLevelMasterView(APIView):

    def get(self,request,pk=None):
        if pk:
            query = LanguagesLevels.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Nivel de lenguaje no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = LanguagesLevelsSerializer(query,context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = LanguagesLevels.objects.all()
        if not query:
            return Response({'error':'No hay nivel de lenguaje.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = LanguagesLevelsSerializer(query,many = True,context={'request': request})
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = LanguagesLevelsSerializer(data=request.data,context={'request': request})
        data.is_valid(raise_exception=True)
        validatedData = LanguagesLevels.objects.filter(language_level__iexact=data.validated_data['language_level']).first()
        if validatedData:
            return Response({'error':'El nivel lenguaje que intenta crear ya existe'},status=status.HTTP_400_BAD_REQUEST)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = LanguagesLevels.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = LanguagesLevelsSerializer(query,data=request.data,context={'request': request})
        serializedQuery.is_valid(raise_exception=True)
        validatedData = LanguagesLevels.objects.filter(language_level__iexact=serializedQuery.validated_data['language_level']).first()
        if validatedData:
            return Response({'error':'El nivel lenguaje que intenta actualizar ya existe'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery.save()
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = LanguagesLevels.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        
        query.delete()
        return Response({'response':'Eliminado con éxito.'},status=status.HTTP_200_OK)

class AreasMasterView(APIView):

    def get(self,request,pk=None):
        if pk:
            query = Areas.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Área no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = AreasSerializer(query, context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = Areas.objects.all()
        if not query:
            return Response({'error':'No hay áreas.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = AreasSerializer(query,many = True, context={'request': request})
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = AreasSerializer(data=request.data, context={'request': request})
        data.is_valid(raise_exception=True)
        validatedData = Areas.objects.filter(area_name__iexact=data.validated_data['area_name'])
        if validatedData:
            return Response({'error':'El área que intenta crear ya existe'},status=status.HTTP_400_BAD_REQUEST)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Areas.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = AreasSerializer(query,data=request.data,context={'request': request})
        serializedQuery.is_valid(raise_exception=True)
        validatedData = Areas.objects.filter(area_name__iexact=serializedQuery.validated_data['area_name'])
        if validatedData:
            return Response({'error':'El área que intenta actualizar ya existe'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery.save()
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Areas.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        
        query.delete()
        return Response({'response':'Eliminado con éxito.'},status=status.HTTP_200_OK)

class LevelMasterView(APIView):

    def validate_existing_area(self,request,instance,action):
        try:
            areas = request.data.pop('areas') 
            areas = [x.get('id') for x in areas]
        except:
            areas = None
        # breakpoint()
        if areas:
            if action == 'create' :
                sendToLanguagesLevelsRel = [LevelsAreas(area_id=Areas.objects.filter(id=x).first(),level_id=instance) for x in areas]
                LevelsAreas.objects.bulk_create(sendToLanguagesLevelsRel) 
            else :
                if not request.data.get('toDelete'):
                    existingAreasIds = AreasFromLevelsSerializer(instance,context={'request':request})
                    for x in existingAreasIds.data.get('areas'):
                        areas.remove(x.get('area_id').get('id'))
                    try:
                        sendToLanguagesLevelsRel = [LevelsAreas(area_id=Areas.objects.filter(id=x).first(),level_id=instance) for x in areas]
                        LevelsAreas.objects.bulk_create(sendToLanguagesLevelsRel)
                    except:
                        pass
                else:
                    query = LevelsAreas.objects.filter(area_id__in=request.data.get('toDelete'),level_id=instance.id)
                    query.delete()
    
    def get(self,request,pk=None):

        if pk:
            query = Levels.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Nivel no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = LevelsSerializer(query,context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = Levels.objects.all()
        if not query:
            return Response({'error':'No hay Nivel.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = LevelsSerializer(query,many = True,context={'request': request})
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = LevelsSerializer(data=request.data,context={'request': request})

        data.is_valid(raise_exception=True)
        validatedData = Levels.objects.filter(level_name__iexact=data.validated_data['level_name'])
        if validatedData:
            return Response({'error':'El nivel que intenta crear ya existe'},status=status.HTTP_400_BAD_REQUEST)
        instance = data.save()
        self.validate_existing_area(request,instance,'create')
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Levels.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = LevelsSerializer(query,data=request.data,context={'request': request})
        serializedQuery.is_valid(raise_exception=True)
        validatedData = Levels.objects.filter(level_name__iexact=serializedQuery.validated_data['level_name'])
        if validatedData:
            return Response({'error':'El nivel que intenta actualizar ya existe.'},status=status.HTTP_400_BAD_REQUEST)
        instance = serializedQuery.save()
        self.validate_existing_area(request,instance,'update')
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Levels.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        
        query.delete()
        return Response({'response':'Eliminado con éxito.'},status=status.HTTP_200_OK)

#THIS ENDPOINT RETURN LEVELS AND ITS VINCULATED AREAS: LEVEL{"ID":...,AREAS:[{AREA_ID:...},{AREA_ID:...},...]}
class LevelsRelatedAreasView(APIView):
    def get (self,request,*args,**kwargs):
        if request.query_params.get('level'):
            query = Levels.objects.filter(id=request.query_params.get('level')).last()
            if not query:
                return Response({'error':'Nivel no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = AreasFromLevelsSerializer(query,context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        
        query = Levels.objects.all()
        if not query:
            return Response({'error':'Nivel no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = AreasFromLevelsSerializer(query,context={'request': request},many = True)
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)

#THIS ENDPOINT RETURN LANGUAGES AND ITS REALTED LANGUAGELEVELS
class LanguagesLanguagesLevelsView(APIView):
    def get (self,request,*args,**kwargs):  
        query = LanguagesLanguagesLevels.objects.all()
        if not query:
            return Response({'error':'Conexiones de lenguaje y nivel no encontradas.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = LanguagesLanguagesLevelsListSerializer(query,context={'request': request},many = True)
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = LanguagesLanguagesLevelsSerializer(data=request.data,context={'request':request})
        data.is_valid(raise_exception=True)
        validateData = LanguagesLanguagesLevels.objects.filter(language_level_id=data.validated_data['language_level_id'],language_id=data.validated_data['language_id'])
        if validateData:
            return Response({'error':'Ya existe esta relación'},status=status.HTTP_400_BAD_REQUEST)
        data.save()
        return Response({'response':'Creado con éxito'},status=status.HTTP_201_CREATED)

class LevelsAreasMasterView(APIView):

    def get(self,request,pk=None,*args,**kwargs):
        
        #FILTER BY LEVEL
        if request.query_params.get('level_id__in'):
            params = request.query_params.get('level_id__in')
            params = tuple(params.replace(',',''))
            query = LevelsAreas.objects.filter(level_id__in=params)
            if not query:
                return Response({'error':'Item no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = LevelsAreasSerializer(query, many = True,context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        if request.query_params.get('level_id'):
            query = LevelsAreas.objects.filter(level_id=request.query_params.get('level_id'))
            if not query:
                return Response({'error':'Item no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = LevelsAreasSerializer(query,many = True)
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)

        #FILTER BY AREA
        if request.query_params.get('area_id__in'):
            params = request.query_params.get('area_id__in')
            params = tuple(params.replace(',',''))
            query = LevelsAreas.objects.filter(area_id__in=params)
            if not query:
                return Response({'error':'Item no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = LevelsAreasSerializer(query, many = True,context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        if request.query_params.get('area_id'):
            query = LevelsAreas.objects.filter(area_id=request.query_params.get('area_id'))
            if not query:
                return Response({'error':'Item no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = LevelsAreasSerializer(query,many = True)
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)

        #ALL OBJECTS
        query = LevelsAreas.objects.all()
        if not query:
            return Response({'error':'No hay item.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = LevelsAreasSerializer(query,many = True,context={'request': request})
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        # breakpoint()
        data = LevelsAreasSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        validatedData = LevelsAreas.objects.filter(area_id=data.validated_data['area_id'],level_id=data.validated_data['level_id']).last()
        if validatedData:
            return Response({'error':'La conexión que intenta crear ya existe'},status=status.HTTP_400_BAD_REQUEST)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = LevelsAreas.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = LevelsAreasSerializer(query,data=request.data)
        serializedQuery.is_valid(raise_exception=True)
        validatedData = LevelsAreas.objects.filter(area_id=serializedQuery.validated_data['area_id'],level_id=serializedQuery.validated_data['level_id']).last()
        if validatedData:
            return Response({'error':'La conexión que intenta actualizar ya existe.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery.save()
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request):
        if not request.query_params.get('area_id') and not request.query_params.get('level_id'):
            return Response({'error':'Ningún id suministrado, envía area_id o level_id'},status=status.HTTP_400_BAD_REQUEST)
        
        query = LevelsAreas.objects.filter(area_id=request.query_params.get('area_id'),level_id=request.query_params.get('level_id')).last()
        if not query:
            return Response({'error':'Item no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        
        query.delete()
        return Response({'response':'Eliminado con éxito.'},status=status.HTTP_200_OK)

class ProfessionMasterView(APIView):

    def get(self,request,pk=None):
        if pk:
            query = Profession.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Profesión no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = ProfessionSerializer(query,context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = Profession.objects.all()
        if not query:
            return Response({'error':'No hay profesión.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = ProfessionSerializer(query,many = True,context={'request': request})
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = ProfessionSerializer(data=request.data,context={'request': request})
        data.is_valid(raise_exception=True)
        validatedData = Profession.objects.filter(profession_name__iexact=data.validated_data['profession_name'])
        if validatedData:
            return Response({'error':'La profesión que intenta crear ya existe'},status=status.HTTP_400_BAD_REQUEST)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Profession.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = ProfessionSerializer(query,data=request.data,context={'request': request})
        serializedQuery.is_valid(raise_exception=True)
        validatedData = Profession.objects.filter(profession_name__iexact=serializedQuery.validated_data['profession_name'])
        if validatedData:
            return Response({'error':'Los datos que intenta actualizar ya están creados.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery.save()
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Profession.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        
        query.delete()
        return Response({'response':'Eliminado con éxito.'},status=status.HTTP_200_OK)

class ProfessionDegreeMasterView(APIView):

    def get(self,request,pk=None):
        if pk:
            query = ProfessionDegree.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Título no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = ProfessionDegreeSerializer(query,context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = ProfessionDegree.objects.all()
        if not query:
            return Response({'error':'No hay Título.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = ProfessionDegreeSerializer(query,many = True,context={'request': request})
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = ProfessionDegreeSerializer(data=request.data,context={'request': request})
        data.is_valid(raise_exception=True)
        validatedData = ProfessionDegree.objects.filter(profession_degree_name__iexact=data.validated_data['profession_degree_name'])
        if validatedData:
            return Response({'error':'El título que intenta crear ya existe'},status=status.HTTP_400_BAD_REQUEST)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = ProfessionDegree.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = ProfessionDegreeSerializer(query,data=request.data,context={'request': request})
        serializedQuery.is_valid(raise_exception=True)
        validatedData = ProfessionDegree.objects.filter(profession_degree_name__iexact=serializedQuery.validated_data['profession_degree_name'])
        if validatedData:
            return Response({'error':'La información que intenta actualizar ya está creada.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery.save()
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = ProfessionDegree.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        
        query.delete()
        return Response({'response':'Eliminado con éxito.'},status=status.HTTP_200_OK)

class InternalContactsMasterView(APIView):

    def get(self,request,pk=None):
        if pk:
            query = InternalContacts.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Contacto no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = InternalContactsSerializer(query,context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = InternalContacts.objects.all()
        if not query:
            return Response({'error':'No hay contacto.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = InternalContactsSerializer(query,many = True,context={'request': request})
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = InternalContactsSerializer(data=request.data,context={'request': request})
        data.is_valid(raise_exception=True)
        validatedData = InternalContacts.objects.filter(internal_contacts_name__iexact=data.validated_data['internal_contacts_name'])
        if validatedData:
            return Response({'error':'El contacto interno que intenta crear ya existe'},status=status.HTTP_400_BAD_REQUEST)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = InternalContacts.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = InternalContactsSerializer(query,data=request.data,context={'request': request})
        serializedQuery.is_valid(raise_exception=True)
        validatedData = InternalContacts.objects.filter(internal_contacts_name__iexact=serializedQuery.validated_data['internal_contacts_name'])
        if validatedData:
            return Response({'error':'Ya existe un contacto interno con la información que desea actualizar'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery.save()
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = InternalContacts.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        
        query.delete()
        return Response({'response':'Eliminado con éxito.'},status=status.HTTP_200_OK)

class InternalRelationsObjetivesMasterView(APIView):

    def get(self,request,pk=None):
        if pk:
            query = InternalRelationsObjetives.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Relación de contacto no encontrada.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = InternalRelationsObjetivesSerializer(query,context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = InternalRelationsObjetives.objects.all()
        if not query:
            return Response({'error':'No hay relación de contacto.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = InternalRelationsObjetivesSerializer(query,many = True,context={'request': request})
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = InternalRelationsObjetivesSerializer(data=request.data,context={'request': request})
        data.is_valid(raise_exception=True)
        validatedData = InternalRelationsObjetives.objects.filter(Internal_relations_objetives_name__iexact=data.validated_data['Internal_relations_objetives_name'])
        if validatedData:
            return Response({'error':'El objetivo de contacto interno que intenta crear ya existe'},status=status.HTTP_400_BAD_REQUEST)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = InternalRelationsObjetives.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = InternalRelationsObjetivesSerializer(query,data=request.data,context={'request': request})
        serializedQuery.is_valid(raise_exception=True)
        validatedData = InternalRelationsObjetives.objects.filter(Internal_relations_objetives_name__iexact=serializedQuery.validated_data['Internal_relations_objetives_name'])
        if validatedData:
            return Response({'error':'Ya existe la información que intenta actualizar.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery.save()
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = InternalRelationsObjetives.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        
        query.delete()
        return Response({'response':'Eliminado con éxito.'},status=status.HTTP_200_OK)

class ExternalContactsMasterView(APIView):

    def get(self,request,pk=None):
        if pk:
            query = ExternalContacts.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Contacto no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = ExternalContactsSerializer(query,context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = ExternalContacts.objects.all()
        if not query:
            return Response({'error':'No hay contacto.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = ExternalContactsSerializer(query,many = True,context={'request': request})
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = ExternalContactsSerializer(data=request.data,context={'request': request})
        data.is_valid(raise_exception=True)
        validatedData = ExternalContacts.objects.filter(External_contacts_name__iexact=data.validated_data['External_contacts_name'])
        if validatedData:
            return Response({'error':'El objetivo de contacto externo que intenta crear ya existe'},status=status.HTTP_400_BAD_REQUEST)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = ExternalContacts.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = ExternalContactsSerializer(query,data=request.data,context={'request': request})
        serializedQuery.is_valid(raise_exception=True)
        validatedData = ExternalContacts.objects.filter(External_contacts_name__iexact=serializedQuery.validated_data['External_contacts_name'])
        if validatedData:
            return Response({'error':'Ya existe un contacto externo con la información que desea actualizar'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery.save()
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = ExternalContacts.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        
        query.delete()
        return Response({'response':'Eliminado con éxito.'},status=status.HTTP_200_OK)

class ExternalRelationsObjetivesMasterView(APIView):

    def get(self,request,pk=None):
        if pk:
            query = ExternalRelationsObjetives.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Relación de contacto no encontrada.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = ExternalRelationsObjetivesSerializer(query,context={'request': request})
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = ExternalRelationsObjetives.objects.all()
        if not query:
            return Response({'error':'No hay relación de contacto.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = ExternalRelationsObjetivesSerializer(query,many = True,context={'request': request})
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = ExternalRelationsObjetivesSerializer(data=request.data,context={'request': request})
        data.is_valid(raise_exception=True)
        validatedData = ExternalRelationsObjetives.objects.filter(External_relations_objetives_name__iexact=data.validated_data['External_relations_objetives_name'])
        if validatedData:
            return Response({'error':'El objetivo de contacto externo que intenta crear ya existe'},status=status.HTTP_400_BAD_REQUEST)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = ExternalRelationsObjetives.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = ExternalRelationsObjetivesSerializer(query,data=request.data,context={'request': request})
        serializedQuery.is_valid(raise_exception=True)
        validatedData = ExternalRelationsObjetives.objects.filter(External_relations_objetives_name__iexact=serializedQuery.validated_data['External_relations_objetives_name'])
        if validatedData:
            return Response({'error':'Ya existe la información que intenta actualizar.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery.save()
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = ExternalRelationsObjetives.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        
        query.delete()
        return Response({'response':'Eliminado con éxito.'},status=status.HTTP_200_OK)