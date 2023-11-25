from django.contrib import admin
from .models import ServicePage, Project, Testomonial, GalleryImg, Video

admin.site.register(Video)

# Register your models here.
@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    list_display = ('id', 'Service_Title')


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'Project_name', 'Project_content')


@admin.register(Testomonial)
class TestomonialsAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'clint_coments', 'name', 'city')


@admin.register(GalleryImg)
class GalleryImgAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'Service_Name')

