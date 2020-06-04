from django.db import models
from django.conf import settings
from ckeditor.fields import RichTextField
from userdata.models import Roles, DatosUser, Habilidades, DetaRoles, rates


 
class TipoDocu(models.Model):
    nombTipoDoc = models.CharField(max_length = 255, verbose_name="Nombre del tipo de proyecto")
 
    class Meta:
        verbose_name="Tipo de documentos de los proyectos"
        verbose_name_plural="Tipos de proyecto"
 
    def __str__(self):
        return self.nombTipoDoc
    
    
 
class CategProye(models.Model):
    lenguaje = models.CharField(max_length = 255, verbose_name="Lenguaje que se utlizo en el proyecto")
    motorDB = models.CharField(max_length = 255, verbose_name="Motor de base de datos utilizado en el proyecto")
    arquitectura = models.CharField(max_length = 255, verbose_name="Arquitectura del proyecto")
 
    class Meta:
        verbose_name="Categorias de los proyectos"
        verbose_name_plural="Categorias"
 
    def __str__(self):
        return self.arquitectura
 
    


 
class Proyects(models.Model):
    nombProyec = models.CharField(max_length = 255, verbose_name="Nombre del Proyecto")
    descProyec = models.CharField(max_length = 255, verbose_name="Descripción del proyecto")
    imgProyec = models.CharField(max_length = 255, verbose_name="Imagen Del proyecto", default="user.png")
    urlRepo = models.CharField(max_length = 100, verbose_name="Link del repositorio")
    idCateProyec = models.ForeignKey(CategProye, on_delete = models.CASCADE, verbose_name="Identificación de la categoria del proyecto")
    fechaInicio = models.DateTimeField(auto_now_add = False, verbose_name ='Fue iniciado el')
    fechaFinal = models.DateTimeField(auto_now_add = False, verbose_name ='Fue terminado el')
    statusProjecto = models.CharField(max_length = 255, verbose_name="Estado del proyecto")
 
    class Meta:
        verbose_name="Projectos de los usuarios"
        verbose_name_plural="Projectos"
 
    def __str__(self):
        return self.nombProyec


 
class Documents(models.Model):
    nombDocu = models.CharField(max_length = 255, verbose_name="Nombre del Documento")
    pathDocu = models.CharField(max_length = 255, verbose_name="Ruta del documento")
    idTipoDocu = models.ForeignKey(TipoDocu , on_delete = models.CASCADE, verbose_name="Identificación del tipo de proyecto")
    idProyecto = models.ForeignKey(Proyects , on_delete = models.CASCADE, verbose_name="Identificación del proyecto")
    idUsuario = models.ForeignKey(DatosUser , on_delete = models.CASCADE, verbose_name="Identificación del usuario")
    
    class Meta:
        verbose_name="Documentos del proyecto"
        verbose_name_plural="Documentos"
 
    def __str__(self):
        return self.nombDocu

 

