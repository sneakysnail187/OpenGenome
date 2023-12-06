from django.contrib import admin

from .models import Result, Comment, UserCSV, CSVNames

admin.site.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'created_on')
    list_filter = ('created_on')
    search_fields = ('name', 'comment')

admin.site.register(Result)
admin.site.register(UserCSV)
admin.site.register(CSVNames)