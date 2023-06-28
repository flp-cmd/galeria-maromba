from django.contrib import admin

from galeria.models import Exercicios

class ListarExercicios(admin.ModelAdmin):
    list_display = ('id', 'nome', 'categoria', 'publicada')
    list_display_links = ('id', 'nome')
    list_editable = ('publicada', )
    


admin.site.register(Exercicios, ListarExercicios)