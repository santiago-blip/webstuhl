from email.policy import default
from django.db import models
from apps.users.models import Users,Prospects

# Create your models here.
class Vacancies(models.Model):
    users_id = models.ForeignKey(Users,null=True,on_delete=models.SET_NULL)
    denomination = models.CharField(max_length=255)
    years_of_experience = models.IntegerField()
    purpose = models.CharField(max_length=255)
    immediate_position_superior = models.CharField(max_length=255)
    aditional_knowledge = models.CharField(max_length=255)
    responsabilities = models.CharField(max_length=255)
    laboral_conditions = models.CharField(max_length=255)
    competencies = models.CharField(max_length=255)
    date_of_entry = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField()
    prospects_limits = models.IntegerField()

class VacanciesProspects(models.Model):
    vacancies_id = models.ForeignKey(Vacancies,on_delete=models.CASCADE)
    prospects_id = models.ForeignKey(Prospects,on_delete=models.CASCADE)


class InternalContacts(models.Model):
    internal_contacts_name = models.CharField(max_length=255)

class VacanciesInternalContacts(models.Model):
    internal_contacts_id = models.ForeignKey(InternalContacts,on_delete=models.CASCADE)
    vacancies_id = models.ForeignKey(Vacancies,on_delete=models.CASCADE)

class ExternalContacts(models.Model):
    External_contacts_name = models.CharField(max_length=255)

class VacanciesExternalContacts(models.Model):
    External_contacts_id = models.ForeignKey(ExternalContacts,on_delete=models.CASCADE)
    vacancies_id = models.ForeignKey(Vacancies,on_delete=models.CASCADE)

class ExternalRelationsObjetives(models.Model):
    External_relations_objetives_name = models.CharField(max_length=255)

class VacanciesExternalRelationsObjetives(models.Model):
    External_relations_objetives_id = models.ForeignKey(ExternalRelationsObjetives,on_delete=models.CASCADE)
    vacancies_id = models.ForeignKey(Vacancies,on_delete=models.CASCADE)

class InternalRelationsObjetives(models.Model):
    Internal_relations_objetives_name = models.CharField(max_length=255)

class VacanciesInternalRelationsObjetives(models.Model):
    Internal_relations_objetives_id = models.ForeignKey(InternalRelationsObjetives,on_delete=models.CASCADE)
    vacancies_id = models.ForeignKey(Vacancies,on_delete=models.CASCADE)

class Areas(models.Model):
    area_name = models.CharField(max_length=255)
    area_description = models.CharField(max_length=255)

class VacanciesAreas(models.Model):
    areas_id = models.ForeignKey(Areas,on_delete=models.CASCADE)
    vacancies_id = models.ForeignKey(Vacancies,on_delete=models.CASCADE)

class Levels(models.Model):
    level_name = models.CharField(max_length=255)
    level_description = models.CharField(max_length=255)

class VacanciesLevels(models.Model):
    levels_id = models.ForeignKey(Levels,on_delete=models.CASCADE)
    vacancies_id = models.ForeignKey(Vacancies,on_delete=models.CASCADE)

class Languages(models.Model):
    language_name = models.CharField(max_length=255)

class LanguagesLevels(models.Model):
    language_level = models.CharField(max_length=2)

class LanguagesLanguagesLevels(models.Model):
    language_id = models.ForeignKey(Languages,on_delete=models.CASCADE)
    language_level_id = models.ForeignKey(LanguagesLevels,on_delete=models.CASCADE)

class LevelsAreas(models.Model):# nivel tiene muchas areas
    area_id = models.ForeignKey(Areas,on_delete=models.CASCADE)
    level_id = models.ForeignKey(Levels,on_delete=models.CASCADE)

class VacanciesLanguages(models.Model):
    language_id = models.ForeignKey(Languages,on_delete=models.CASCADE)
    vacancies_id = models.ForeignKey(Vacancies,on_delete=models.CASCADE)

class Profession(models.Model):
    profession_name = models.CharField(max_length=255)

class VacanciesProfession(models.Model):
    profession_id = models.ForeignKey(Profession,on_delete=models.CASCADE)
    vacancies_id = models.ForeignKey(Vacancies,on_delete=models.CASCADE)

class ProfessionDegree(models.Model):
    profession_degree_name = models.CharField(max_length=255)

class VacanciesProfessionDegree(models.Model):
    profession_degree_id = models.ForeignKey(ProfessionDegree,on_delete=models.CASCADE)
    vacancies_id = models.ForeignKey(Vacancies,on_delete=models.CASCADE)