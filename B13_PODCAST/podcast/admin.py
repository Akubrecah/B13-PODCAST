# podcasts/admin.py
from django.urls import path
from django.views.generic import TemplateView
from django.contrib import admin

admin.site.site_header = "Podcast Admin"

class PodcastAdmin(admin.ModelAdmin):
    change_list_template = "admin/podcast_changelist.html"

admin.site.register(Podcast, PodcastAdmin)