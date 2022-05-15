from django.contrib import admin

# Register your models here.

from .models import Announcement


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_time', 'modified_time']
    fields = ['title', 'author', 'body', 'category']


admin.site.register(Announcement, AnnouncementAdmin)
