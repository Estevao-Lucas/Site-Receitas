from django.contrib import admin
from django.contrib.admin.filters import ListFilter
from .models import Receita

#Otimizando o admin
class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicada') #mostra esses titulos no admin
    list_display_links = ('id', 'nome_receita') #link para alterar os dados 
    search_fields = ('nome_receita',) #Campo para procurar uma receita pelo nome
    list_filter = ('categoria',) #Filtrar as receitas por categoria
    list_editable = ('publicada',)
    list_per_page = 5 # receitas por página

admin.site.register(Receita, ListandoReceitas)
# Register your models here.
