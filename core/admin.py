from django.contrib import admin
from core.models import Evento
# Register your models here.

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'data_evento', 'data_criacao') #lista os atributos a serem mostrados no admin
    list_filter = ('titulo', 'data_evento') #adiciona um filtro no admin do django

admin.site.register(Evento, EventoAdmin) #Associa as classes
