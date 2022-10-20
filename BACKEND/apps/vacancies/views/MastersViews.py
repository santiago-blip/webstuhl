from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from apps.vacancies.models import (Languages, Areas, Levels, Profession, ProfessionDegree,InternalContacts,
InternalRelationsObjetives,ExternalContacts,ExternalRelationsObjetives)

from apps.vacancies.serializers.MastersSerializer import (LanguagesSerializer,AreasSerializer,LevelsSerializer, ProfessionSerializer,
ProfessionDegreeSerializer, InternalContactsSerializer,InternalRelationsObjetivesSerializer, ExternalContactsSerializer, ExternalRelationsObjetivesSerializer)

class LanguagesMasterView(APIView):

    def get(self,request,pk=None):
        if pk:
            query = Languages.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Lenguaje no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = LanguagesSerializer(query)
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = Languages.objects.all()
        if not query:
            return Response({'error':'No hay lenguajes.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = LanguagesSerializer(query,many = True)
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = LanguagesSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Languages.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = LanguagesSerializer(query,data=request.data)
        serializedQuery.is_valid(raise_exception=True)
        serializedQuery.save()
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Languages.objects.filter(id=pk).first()
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
            serializedQuery = AreasSerializer(query)
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = Areas.objects.all()
        if not query:
            return Response({'error':'No hay áreas.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = AreasSerializer(query,many = True)
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = AreasSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Areas.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = AreasSerializer(query,data=request.data)
        serializedQuery.is_valid(raise_exception=True)
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

    def get(self,request,pk=None):
        if pk:
            query = Levels.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Nivel no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = LevelsSerializer(query)
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = Levels.objects.all()
        if not query:
            return Response({'error':'No hay Nivel.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = LevelsSerializer(query,many = True)
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = LevelsSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Levels.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = LevelsSerializer(query,data=request.data)
        serializedQuery.is_valid(raise_exception=True)
        serializedQuery.save()
        return Response({'response':'Actualizado con éxito.'},status=status.HTTP_200_OK)
    
    def delete(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Levels.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
        
        query.delete()
        return Response({'response':'Eliminado con éxito.'},status=status.HTTP_200_OK)

class ProfessionMasterView(APIView):

    def get(self,request,pk=None):
        if pk:
            query = Profession.objects.filter(id=pk).first()
            if not query:
                return Response({'error':'Profesión no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            serializedQuery = ProfessionSerializer(query)
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = Profession.objects.all()
        if not query:
            return Response({'error':'No hay profesión.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = ProfessionSerializer(query,many = True)
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = ProfessionSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = Profession.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = ProfessionSerializer(query,data=request.data)
        serializedQuery.is_valid(raise_exception=True)
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
            serializedQuery = ProfessionDegreeSerializer(query)
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = ProfessionDegree.objects.all()
        if not query:
            return Response({'error':'No hay Título.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = ProfessionDegreeSerializer(query,many = True)
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = ProfessionDegreeSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = ProfessionDegree.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = ProfessionDegreeSerializer(query,data=request.data)
        serializedQuery.is_valid(raise_exception=True)
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
            serializedQuery = InternalContactsSerializer(query)
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = InternalContacts.objects.all()
        if not query:
            return Response({'error':'No hay contacto.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = InternalContactsSerializer(query,many = True)
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = InternalContactsSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = InternalContacts.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = InternalContactsSerializer(query,data=request.data)
        serializedQuery.is_valid(raise_exception=True)
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
            serializedQuery = InternalRelationsObjetivesSerializer(query)
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = InternalRelationsObjetives.objects.all()
        if not query:
            return Response({'error':'No hay relación de contacto.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = InternalRelationsObjetivesSerializer(query,many = True)
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = InternalRelationsObjetivesSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = InternalRelationsObjetives.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = InternalRelationsObjetivesSerializer(query,data=request.data)
        serializedQuery.is_valid(raise_exception=True)
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
            serializedQuery = ExternalContactsSerializer(query)
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = ExternalContacts.objects.all()
        if not query:
            return Response({'error':'No hay contacto.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = ExternalContactsSerializer(query,many = True)
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = ExternalContactsSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = ExternalContacts.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = ExternalContactsSerializer(query,data=request.data)
        serializedQuery.is_valid(raise_exception=True)
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
            serializedQuery = ExternalRelationsObjetivesSerializer(query)
            return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
        query = ExternalRelationsObjetives.objects.all()
        if not query:
            return Response({'error':'No hay relación de contacto.'},status=status.HTTP_400_BAD_REQUEST)
        serializedQuery = ExternalRelationsObjetivesSerializer(query,many = True)
        return Response({'response':serializedQuery.data},status=status.HTTP_200_OK)
    
    def post(self,request):
        data = ExternalRelationsObjetivesSerializer(data=request.data)
        data.is_valid(raise_exception=True)
        data.save()
        return Response({'response':'Creado con éxito.'},status=status.HTTP_201_CREATED)
    
    def put(self,request,pk=None):
        if not pk:
            return Response({'error':'id no válido.'},status=status.HTTP_400_BAD_REQUEST)
        
        query = ExternalRelationsObjetives.objects.filter(id=pk).first()
        if not query:
            return Response({'error':'id no encontrado.'},status=status.HTTP_400_BAD_REQUEST)
            
        serializedQuery = ExternalRelationsObjetivesSerializer(query,data=request.data)
        serializedQuery.is_valid(raise_exception=True)
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