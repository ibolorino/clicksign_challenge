from django.contrib import admin

from .models import Folder


class FolderAdmin(admin.ModelAdmin):
    exclude = ("level",)


admin.site.register(Folder)
