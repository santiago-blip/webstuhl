from email.policy import default
from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


documentTypes = [
        ('C.C', 'Cédula de ciudadanía'),
        ('NIT', 'NIT'),
        ('C.E', 'Cédula de extranjería'),
        ('T.I','Tarjeta de identidad')
    ]

#PROSPECTOS
class Prospects(models.Model):
    stateTypes = [
            ('ENP', 'En proceso'),
            ('AP', 'Aplicó'),
            ('NP', 'Ningún proceso')
        ]
    name = models.CharField('Nombres', max_length = 255)
    last_name = models.CharField('Apellidos', max_length = 255)
    document_type = models.CharField('Tipo de documento', max_length = 3, choices=documentTypes)
    document_number = models.CharField('Número de documento', max_length = 255)
    waiting_list= models.BooleanField(default = False)
    prospect_cv = models.CharField('Hoja de vida',max_length=255)
    postulated_date = models.DateTimeField(auto_now_add=True)
    state= models.CharField('Estado del proceso', max_length = 3, choices=stateTypes,default='NP')

#MODELOS DE USUARIO
class UserManager(BaseUserManager):
    def _create_user(self, username, email, name,last_name, password, is_superuser, **extra_fields):
        user = self.model(
            username = username,
            email = email,
            name = name,
            last_name = last_name,
            is_superuser = is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password, False, **extra_fields)

    def create_superuser(self, username, email, name,last_name, password=None, **extra_fields):
        return self._create_user(username, email, name,last_name, password,True, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):

    username = models.CharField(max_length = 255, unique = True)
    email = models.EmailField('Correo Electrónico',max_length = 255, unique = True,)
    password = models.CharField('Contraseña',max_length = 255)
    name = models.CharField('Nombres', max_length = 255)
    last_name = models.CharField('Apellidos', max_length = 255)
    document_type = models.CharField('Tipo de documento', max_length = 3, choices=documentTypes)
    document_number = models.CharField('Número de documento', max_length = 255)
    image = models.ImageField('Imagen de perfil', upload_to='perfil/', max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    deactivated_date = models.DateTimeField(auto_now=False, auto_now_add=False,null = True, blank = True)
    is_active = models.BooleanField(default = True)
    is_superuser= models.BooleanField(default = False)
    prospect = models.ForeignKey(Prospects,on_delete=models.CASCADE,null=True,blank=True)
    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']

    @property
    def is_staff(self):
        return self.is_superuser

    # def save(self,*args,**kwargs):
    #     self.set_password(self.password)
    #     super(User,self).save(*args,**kwargs)

    def __str__(self):
        return f'{self.name} {self.last_name}'

class Groups(models.Model):
    name = models.CharField('Nombre',max_length = 255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    deactivated_date = models.DateTimeField(auto_now=False, auto_now_add=False,null = True, blank = True)


class Permissions(models.Model):
    name = models.CharField('Nombre',max_length = 255)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    deactivated_date = models.DateTimeField(auto_now=False, auto_now_add=False,null = True, blank = True)


class UsersGroups(models.Model):
    groups_id = models.ForeignKey(Groups,on_delete=models.CASCADE)
    users_id = models.ForeignKey(Users,on_delete=models.CASCADE)



class UsersPermissions(models.Model):
    permissions_id = models.ForeignKey(Permissions,on_delete=models.CASCADE)
    users_id = models.ForeignKey(Users,on_delete=models.CASCADE)

class PermissionsGroups(models.Model):
    permissions_id = models.ForeignKey(Permissions,on_delete=models.CASCADE)
    groups_id = models.ForeignKey(Groups,on_delete=models.CASCADE)
