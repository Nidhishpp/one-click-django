from django.contrib import admin
from .models import *

class adminService(admin.ModelAdmin):
     list_display=('title','image','description','feature','price','category_title','featured','visible')
     def category_title(self, instance):
            return instance.category.title

class adminCategory(admin.ModelAdmin):
    
    list_display=('title','image','featured')

admin.site.register(service,adminService)
admin.site.register(category,adminCategory)
admin.site.register(comments)
