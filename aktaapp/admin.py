from django.contrib import admin
from .models import Stanowiska, Pracownicy

@admin.register(Stanowiska)
class StanowiskaAdmin(admin.ModelAdmin):
    pass
@admin.register(Pracownicy)
class PracownicyAdmin(admin.ModelAdmin):
    pass
