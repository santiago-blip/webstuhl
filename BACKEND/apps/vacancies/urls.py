from django.urls import path
from apps.vacancies.views.MastersViews import (LanguagesMasterView,AreasMasterView, LevelMasterView,ProfessionMasterView,ProfessionDegreeMasterView,
InternalContactsMasterView,InternalRelationsObjetivesMasterView,ExternalContactsMasterView,ExternalRelationsObjetivesMasterView)

urlpatterns = [
    path('master/languages/',LanguagesMasterView.as_view(),name="masterLanguage"),
    path('master/languages/<int:pk>/',LanguagesMasterView.as_view(),name="masterLanguageId"),
    path('master/areas/',AreasMasterView.as_view(),name="masterArea"),
    path('master/areas/<int:pk>/',AreasMasterView.as_view(),name="masterAreaId"),
    path('master/levels/',LevelMasterView.as_view(),name="masterLevel"),
    path('master/levels/<int:pk>/',LevelMasterView.as_view(),name="masterLevelId"),
    path('master/professions/',ProfessionMasterView.as_view(),name="masterProfession"),
    path('master/professions/<int:pk>/',ProfessionMasterView.as_view(),name="masterProfessionId"),
    path('master/professionsDegree/',ProfessionDegreeMasterView.as_view(),name="masterProfessionDegree"),
    path('master/professionsDegree/<int:pk>/',ProfessionDegreeMasterView.as_view(),name="masterProfessionDegreeId"),
    path('master/internalContacts/',InternalContactsMasterView.as_view(),name="masterInternalContact"),
    path('master/internalContacts/<int:pk>/',InternalContactsMasterView.as_view(),name="masterInternalContactId"),
    path('master/internalRelationsObjetives/',InternalRelationsObjetivesMasterView.as_view(),name="masterinternalRelationsObjetives"),
    path('master/internalRelationsObjetives/<int:pk>/',InternalRelationsObjetivesMasterView.as_view(),name="masterinternalRelationsObjetivesId"),
    path('master/ExternalContacts/',ExternalContactsMasterView.as_view(),name="masterExternalContacts"),
    path('master/ExternalContacts/<int:pk>/',ExternalContactsMasterView.as_view(),name="masterExternalContactsId"),
    path('master/ExternalRelationsObjetives/',ExternalRelationsObjetivesMasterView.as_view(),name="masterExternalRelationsObjetives"),
    path('master/ExternalRelationsObjetives/<int:pk>/',ExternalRelationsObjetivesMasterView.as_view(),name="masterExternalRelationsObjetivesId"),
]