from django.contrib import admin
from registro.models import Consulta,Dentista


class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('nome_do_paciente', 'data', 'hora', 'serviço')
admin.site.register(Consulta,ConsultaAdmin)


class DentistaAdmin(admin.ModelAdmin):
    list_display = ('nome_do_dentista','CRO')
admin.site.register(Dentista, DentistaAdmin)

