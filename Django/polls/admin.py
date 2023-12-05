from django.contrib import admin

from .models import Result, Comment

admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'created_on')
    list_filter = ('created_on')
    search_fields = ('name', 'comment')

admin.site.register(Result)