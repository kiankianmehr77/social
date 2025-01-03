from django.contrib import admin
from .models import Relation

@admin.register(Relation)
class PostAdmin(admin.ModelAdmin):
    list_display = ['from_user', 'to_user']
    list_filter = ('created',)

