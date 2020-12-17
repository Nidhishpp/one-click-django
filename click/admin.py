from django.contrib import admin
from django.contrib.auth.models import Group
from .models import *
import csv
from django.http import HttpResponse

admin.site.site_header = "OneClick"

def export_order(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'
    writer = csv.writer(response)
    writer.writerow(['User','Service','Date','Time','Location','Phone','Payment Id','Status','Booking Date'])
    order = queryset.values_list('user', 'service', 'date', 'time', 'location', 'phn', 'payment_id', 'status', 'booking_date')
    for book in order:
        writer.writerow(book)
    return response

export_order.short_description = 'Export to csv'

class adminService(admin.ModelAdmin):
    list_display = ('title', 'image', 'description', 'feature',
                    'price', 'category_title', 'featured', 'visible')

    def category_title(self, instance):
        return instance.category.title


class adminCategory(admin.ModelAdmin):

    list_display = ('title', 'image', 'featured')


class adminBooking(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "staff":
            kwargs["queryset"] = User.objects.filter(is_staff=1)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

    actions = [ export_order ]

    list_display = ('user', 'service', 'date', 'time',
                    'location', 'phn', 'payment_id', 'status', 'booking_date')
    readonly_fields = ('location', 'user', 'booking_date',
                       'date', 'time', 'service', 'phn', 'payment_id')

    def has_add_permission(self, request, obj=None):
        return False

admin.site.register(service, adminService)
admin.site.register(category, adminCategory)
# admin.site.register(comments)
# admin.site.register(profile)
admin.site.register(booking, adminBooking)
admin.site.unregister(Group)