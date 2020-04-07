from django.contrib import admin
from interesados.models import interesado

@admin.register(interesado)
class interesadoAdmin(admin.ModelAdmin):
# Register your models here.
     list_display = ('telefono', 'nombre', 'creado', 'modificado', 'vendedor', 'estatus', 'ciudad', 'comentarios', 'compro')
     list_display_links = ('telefono',)
     search_fields = ('telefono', 'nombre', 'creado', 'vendedor')
     list_filter = ('compro', 'creado', 'estatus', 'ciudad')
     list_editable = ('estatus', 'vendedor')
     readonly_fields = ('creado',)
     