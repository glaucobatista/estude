from django.contrib import admin
from .models import Categoria, Flashcard, Desafio, FlashcardDesafio

class FlashcardAdmin(admin.ModelAdmin):
    list_display = ['pergunta','categoria','user']

admin.site.register(Categoria)
admin.site.register(Flashcard, FlashcardAdmin)
admin.site.register(Desafio)
admin.site.register(FlashcardDesafio)