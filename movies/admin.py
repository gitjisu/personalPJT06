from django.contrib import admin
from .models import Comment, Movie

class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'content',)

class MovieAdmin(admin.ModelAdmin):
    list_display = ('pk',)    

admin.site.register(Comment, CommentAdmin)
admin.site.register(Movie, MovieAdmin)