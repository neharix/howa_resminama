from django.contrib import admin

from .models import Document, Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["pk", "user"]


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["pk", "filename", "date"]
