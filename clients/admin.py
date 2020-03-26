from django.contrib import admin
from clients.models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('pk','name', 'phone', 'attended')
    list_display_links = ('pk','name', 'phone')
    search_fields = ('name', 'phone')
    list_filter = ('attended', 'created')
    list_editable = ('attended',)

# Register your models here.
