from django.contrib import admin
from .models import Company, Job
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
	list_display = ('name', 'created_at')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Job)