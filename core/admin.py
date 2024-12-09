from django.contrib import admin
from .models import Nurse, NurseShift, Contract

class NurseAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'city', 'specialization', 'created_at')
    search_fields = ('name', 'email', 'city', 'specialization')

admin.site.register(Nurse, NurseAdmin)

class NurseShiftAdmin(admin.ModelAdmin):
    list_display = ('nurse', 'start_time', 'end_time')
    list_filter = ('nurse',)
    search_fields = ('nurse__name', 'nurse__email')

admin.site.register(NurseShift, NurseShiftAdmin)

class ContractAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'uploaded_at')
    list_filter = ('category',)
    search_fields = ('name',)

admin.site.register(Contract, ContractAdmin)
