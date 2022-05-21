from django.contrib import admin
from pages.models import Team
from django.utils.html import format_html # to use html sentax inside python
# Register your models here.

class TeamAdmin(admin.ModelAdmin): # to show all column in table
    def thumbnail(self,object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;"/>'.format(object.photo.url))
    thumbnail.short_description = 'photo'
    list_display  = ('id', 'thumbnail', 'first_name' ,'designation', 'created_date' )
    list_display_links = ('id', 'thumbnail','first_name',) # to make first name column clickable
    search_fields = ('first_name', 'last_name' ,'designation')
    list_filter = ('designation',)
admin.site.register(Team, TeamAdmin)