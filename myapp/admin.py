from django.contrib import admin
from .models import posts,shareholderPattern,compliance,projectEnquary,projectTable,schedulOn,Callback


# Register your models here.
class postsAdmin(admin.ModelAdmin):
    list_display=[
        'title',
        'comments',
        'image',
        'pdf',
        'post_date',
    ]
admin.site.register(posts,postsAdmin)
class shareholderPatternAdmin(admin.ModelAdmin):
    list_display=["year","month","pdf"]
admin.site.register(shareholderPattern,shareholderPatternAdmin)


class complianceAdmin(admin.ModelAdmin):
    list_display=["fy","comp_type","quarter","description","pdf"]
admin.site.register(compliance,complianceAdmin)

class projectEnquaryAdmin(admin.ModelAdmin):
    list_display=[
        "firstName",
        "lastName",
        "email",
        "country",
        "cityName",
        "mobile",
        "projectName"
    ]
admin.site.register(projectEnquary,projectEnquaryAdmin)

class projectTableAdmin(admin.ModelAdmin):
    list_display=[
        "project",
        "price",
        "locality",
        "topology",
        "location",
        "neighbourhood",
        "master_plan",
        "unit_plan",
        "image",
        "image2",
        "image3",
        "image4",
    ]
admin.site.register(projectTable,projectTableAdmin)

class schedulOnAdmin(admin.ModelAdmin):
    list_display=[
        "firstName",
        "lastName",
        "email",
        "country",
        "mobile",
        "schedule_data",
        "schedule_time",
        "projectName",
    ]
admin.site.register(schedulOn,schedulOnAdmin)

class CallbackAdmin(admin.ModelAdmin):
    list_display=[
    "name",
    "country",
    "mobile",
    "email",
    "confirm"
    ]
admin.site.register(Callback,CallbackAdmin)

from myapp.models import amenities,customer,OTP
admin.site.register(amenities)
admin.site.register(OTP)


class customerAdmin(admin.ModelAdmin):
    list_display=[
        "name",
        "mobile",
        "email",
        "countryName",
        "address",
        "password",
        "created_at",
    ]
admin.site.register(customer,customerAdmin)





