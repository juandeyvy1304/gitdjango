from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from .genero import Generos

# Create your models here.
#crear estrucuta base de datos
 
class Roles(models.Model):
    
    RoleName = models.CharField(max_length = 50)

    class Meta:
        verbose_name = "perfiles de usuario"
        verbose_name_plural = "perfiles"
 
    def __str__(self): 
        return self.RoleName
    
class DatosUser(models.Model):
    userDNI = models.CharField(max_length = 25,verbose_name='Identificación')
    nombUser = models.CharField(max_length = 236, null=True, verbose_name='Nombres')
    apelUser = models.CharField(max_length = 236, null=True, verbose_name='Apellido')
    profeUser = models.CharField(max_length = 100, null=True, verbose_name='profesion')
    fotoUser = models.ImageField(default='user.png', verbose_name='Foto de perfil', upload_to="perfiles/img")
    teleUser = models.CharField(max_length = 255, verbose_name='Teléfono')
    geneUser =models.CharField(max_length = 20, choices = Generos, default = "Otro",verbose_name='Genero')
    adddata = models.DateTimeField(auto_now_add = True, null=True, verbose_name ='Fue creado el')
    modifiat = models.DateTimeField(auto_now = True, null=True,  verbose_name = 'Genero modificado')
 
    class Meta:
        verbose_name = "Datos de Usuario"
        verbose_name_plural = "Información"
 
    def __str__(self):
        return self.userDNI
 
class Habilidades(models.Model):
    NombHabil = models.CharField(max_length = 22)
    DescHabil = models.TextField(max_length = 2000, verbose_name = "Descripcion")

    class Meta:
        verbose_name = "habilidades del usuario"
        verbose_name_plural = "competencias"

    def __str_(self):
        return self.NombHabil
 
class DetaRoles(models.Model):
    idRoles = models.ForeignKey(Roles, on_delete = models.CASCADE, verbose_name = "Identificador de rol")
    idUser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    addUser = models.DateTimeField(auto_now_add = True, auto_now = False)
    udtuser = models.DateTimeField(auto_now = True)
    estadoRol = models.CharField(max_length = 19)
 
    class Meta:
        verbose_name = ""
        verbose_name_plural = ""
 
    def __str__(self):
        return self.idUser
 
class rates(models.Model):
    idHabil = models.ForeignKey(Habilidades, on_delete = models.CASCADE)
    iduser = models.ForeignKey(DatosUser, on_delete = models.CASCADE)
    Porcentaje = models.DecimalField(max_digits = 2, decimal_places =1)
    udtHabil = models.DateTimeField(auto_now = True)
 
    class Meta:
        verbose_name = "nivel de habilidades"
        verbose_name_plural = "niveles de usuario"
 
    def __str__(self):
        return self.Porcentaje