from django.contrib import admin
from blog.models import Post,Comment
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','text','created_date','published_date']
    list_filter = ['created_date','author']
    search_fields = ('author','title')

class CommentAdmin(admin.ModelAdmin):
    list_display = ['post','name','text','created_date','active']
    list_filter = ['created_date','post']

admin.site.register(Post,PostAdmin)
admin.site.register(Comment,CommentAdmin)
