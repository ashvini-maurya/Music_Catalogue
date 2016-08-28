from django.contrib import admin
from gaana.models import Artist, Song, UserProfile, Playlist, Like

class ArtistAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}


admin.site.register(Artist, ArtistAdmin)
admin.site.register(Song)
admin.site.register(UserProfile)
admin.site.register(Playlist)
admin.site.register(Like)