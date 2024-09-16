from django.contrib import admin
from medicaments.models import Medicament

# Register your models here.


class MedicamentAdmin(admin.ModelAdmin):
    list_display = ['name', 'quantity', 'expiration_date', 'type_medicament', 'category_medicament', 'owner']
    ordering = ['name', 'expiration_date']
    list_filter = ['type_medicament', 'category_medicament']
    search_fields = ['name']


admin.site.register(Medicament, MedicamentAdmin)
