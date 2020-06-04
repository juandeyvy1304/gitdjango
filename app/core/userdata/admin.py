from django.contrib import admin

from .models import Roles, DatosUser, Habilidades, DetaRoles, rates

class RoleModel(admin.ModelAdmin):
    list_display = ["RoleName"]
    list_display_links = ["RoleName"]
    list_filter = ["RoleName"]
    class Meta:
       model = Roles
admin.site.register(Roles)

class DatosUserModel(admin.ModelAdmin):
    list_display = ["userDNI"]
    list_display_links = ["userDNI"]
    list_filter = ["userDNI"]
    class Meta:
        model = DatosUser
admin.site.register(DatosUser)

class HabilidadesModel(admin.ModelAdmin):
    list_display = ["NombHabil"]
    list_display_links = ["NombHabil"]
    list_filter = ["NombHabil"]
    class Meta:
        model = Habilidades
admin.site.register(Habilidades)

class DetaRolesModel(admin.ModelAdmin):
    list_display = ["idUser"]
    list_display_links = ["idUser"]
    list_filter = ["idUser"]
    class Meta:
        model = DetaRoles
admin.site.register(DetaRoles)

class ratesModel(admin.ModelAdmin):
    list_display = ["Porcentaje"]
    list_display_links = ["Porcentaje"]
    list_filter = ["Porcentaje"]
    class Meta:
        model = rates
admin.site.register(rates)

