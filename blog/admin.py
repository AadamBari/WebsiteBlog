from django.contrib import admin
from .models import Post 

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",) # on admin page gives option to filter posts by status (draft/publish)
    search_fields = ['title', 'content'] # search terms for search bar options 
    prepopulated_fields = {'slug': ('title',)} # slug field will be automatically populated based on title
  
admin.site.register(Post, PostAdmin)