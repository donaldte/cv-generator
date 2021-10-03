from django.contrib import admin

from pdf.models import Profile

# Register your models here.
class AdminProfile(admin.ModelAdmin):
    list_display = ('name', 'email','image', 'phone', 'address', 'competance', 'langue', 'interet', 'objectif', 'experience', 'education', 'Projet')


admin.site.register(Profile, AdminProfile)