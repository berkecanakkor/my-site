from django.contrib import admin
from .models import Blog,Category


# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','is_active','is_home')
    list_filter = ('category', 'is_active', 'is_home')
    
    
admin.site.register(Blog,BlogAdmin)
admin.site.register(Category)
