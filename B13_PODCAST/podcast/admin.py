# podcasts/admin.py
from django.contrib import admin
from .models import Podcast, Episode  # Import your models

admin.site.site_header = "Podcast Admin"
admin.site.site_title = "Podcast Administration"

class EpisodeInline(admin.StackedInline):
    model = Episode
    extra = 1
    fields = ('title', 'audio_file', 'duration', 'created_at')
    readonly_fields = ('created_at',)

class PodcastAdmin(admin.ModelAdmin):
    # Specify the custom change list template
    change_list_template = "admin/podcast_changelist.html"
    
    # Add inlines for managing episodes directly from podcast
    inlines = [EpisodeInline]
    
    # Fields to display in list view
    list_display = ('title', 'host', 'created_at')
    
    # Make podcast creation date read-only
    readonly_fields = ('created_at',)
    
    # Search functionality
    search_fields = ('title', 'description', 'host__username')

# Register both models
admin.site.register(Podcast, PodcastAdmin)
admin.site.register(Episode)