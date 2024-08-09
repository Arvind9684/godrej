from django.contrib import admin
from .models import Picture, City, SubArea, PropertyType, Category, SubCategory, Website, Location, Publisher, Gallery, Project

class ProjectAdmin(admin.ModelAdmin):
    list_display=[
        "name",
        "description",
        "picture",
        "view",
        "is_verified",
        "is_for_rent",
        "title",
        "city",
        "sub_area",
        "property_type",
        "category",
        "sub_category",
        "website",
        "amenities",
        "nearby",
        "expiration_date",
        "construction_status",
        "status",
        "furnished",
        "security_deposit",
        "rent_property",
        "rent_escalation_period",
        "rent_priority_comment",
        "size",
        "carpet_area",
        "type",
        "builder",
        "floor",
        "total_floor",
        "facing",
        "possession_type",
        "is_rented",
        "rent",
        "cost",
        "extra_charge",
        "lease_time",
        "lease_completed",
        "lease_balance",
        "rent_escalation",
        "rent_to",
        "maintenance",
        "registry",
        "transfer_charge",
        "gst",
        "profit_sharing",
        "roi",
        "profile_pic",
        "shop_for",
        "posted_by",
        "possession_status",
        "possession_date",
        "is_corner_plot",
        "hidden_notes",
        "lock_in",
        "power_breakup_rate",
        "road_size",
        "publisher",
        "meta_desc",
        "meta_key",
        "is_distress",
        "reason_distress",
        "cost_distress",
        "recommended",
        "plot_size",
        "construction_age",
        "code",
        "listing_date",
        "slug",
    ]
admin.site.register(Project,ProjectAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display=[
        "is_active",
        "listing",
        "state",
        "city",
        "department",
        "designation",
        "role",
        "name",
        "email",
        "phone",
        "password",
        "address",
        "created_on",
        "pub_id",
        "listing_date",
        "plan_id",
    ]
admin.site.register(Publisher,PublisherAdmin)

class PictureAdmin(admin.ModelAdmin):
    list_display=[
        "project_name",
        "title",
        "image",
    ]
admin.site.register(Picture,PictureAdmin)


class CityAdmin(admin.ModelAdmin):
    list_display=[
        "name"
    ]
admin.site.register(City,CityAdmin)


class subAreaAdmin(admin.ModelAdmin):
    list_display=[
        "name"
    ]
admin.site.register(SubArea,subAreaAdmin)

class PropertyTypeAdmin(admin.ModelAdmin):
    list_display=[
        "name"
    ]
admin.site.register(PropertyType,PropertyTypeAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display=[
        "name"
    ]
admin.site.register(Category,CategoryAdmin)

class subCategryAdmin(admin.ModelAdmin):
    list_display=[
        "name"
    ]
admin.site.register(SubCategory,subCategryAdmin)

class WebsiteAdmin(admin.ModelAdmin):
    list_display=[
        "name"
    ]
admin.site.register(Website,WebsiteAdmin)

class LocationAdmin(admin.ModelAdmin):
    list_display=[
        "city",
        "name",
        "longitude",
        "latitude",
    ]
admin.site.register(Location,LocationAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display=[
        "publisher",
        "image",
    ]
admin.site.register(Gallery,GalleryAdmin)
