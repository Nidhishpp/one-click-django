from django.contrib import admin
from .models import *

class adminService(admin.ModelAdmin):
     list_display=('title','image','description','feature','price','category_title','featured','visible')
     def category_title(self, instance):
            return instance.category.title

class adminCategory(admin.ModelAdmin):
    
    list_display=('title','image','featured')


class adminBooking(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "staff":
            kwargs["queryset"] = User.objects.filter(is_staff=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    list_display=('user','booking_date','date','time','location','status','service','phn')
    readonly_fields=('location','user','booking_date','date','time','service','phn' )
    


   
   


admin.site.register(service,adminService)
admin.site.register(category,adminCategory)
admin.site.register(comments)
admin.site.register(profile)
admin.site.register(booking,adminBooking)

