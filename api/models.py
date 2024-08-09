# api/models.py

from django.db import models
from django.utils import timezone


class City(models.Model):
    name = models.CharField(max_length=255,unique=True)
    def __str__(self):
        return f'City: {self.name}'

class SubArea(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'SubArea: {self.name}'

class PropertyType(models.Model):
    PROP_CHOICES = [
        ('Commercial', 'Commercial'),
        ('Residential', 'Residential'),
    ]
    name = models.CharField(max_length=100, choices=PROP_CHOICES, default='Commercial')
    
    def __str__(self):
        return f'PropertyType: {self.name}'

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'Category: {self.name}'

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'SubCategory: {self.name}'

class Website(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f'Website: {self.name}'

class Location(models.Model):
    city = models.ForeignKey(City, related_name="locations", on_delete=models.CASCADE)
    name = models.CharField(max_length=255,default='')
    longitude = models.CharField(max_length=50,default='')
    latitude = models.CharField(max_length=50,default='')
    
    def __str__(self):
        return f'Location: {self.name} in {self.city.name}'

class Publisher(models.Model):
    is_active = models.BooleanField(default=True)
    listing = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=255,default='')
    city = models.CharField(max_length=255,default='')
    department = models.CharField(max_length=255,default='')
    designation = models.CharField(max_length=255,default='')
    role = models.CharField(max_length=255,default='')
    name = models.CharField(max_length=255,default='')
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20,default='')
    password = models.CharField(max_length=50,default='')
    address = models.TextField(default='')
    created_on = models.DateTimeField(default=timezone.now)
    pub_id = models.CharField(max_length=255,default='')
    listing_date = models.DateTimeField(null=True, blank=True,default='')
    plan_id = models.CharField(max_length=50,default='')
    
    def __str__(self):
        return f'Publisher: {self.name}'

class Gallery(models.Model):
    publisher = models.ForeignKey(Publisher, related_name='galleries', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    
    def __str__(self):
        return f'Gallery Image for {self.publisher.name}'

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default='',null=True)
    picture = models.FileField(upload_to="projects/pictures/", blank=True, null=True)
    view = models.BigIntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    is_for_rent = models.BooleanField(default=False)
    title = models.TextField(default='',null=True)
    city = models.ForeignKey(City, related_name="city", on_delete=models.CASCADE)
    sub_area = models.ForeignKey(SubArea, related_name='sub_area', on_delete=models.CASCADE)
    property_type = models.ForeignKey(PropertyType, related_name='property_type', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, related_name='sub_category', on_delete=models.CASCADE)
    website = models.ForeignKey(Website, related_name='website', on_delete=models.CASCADE)
    amenities = models.TextField(default='',null=True)
    nearby = models.TextField(default='',null=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    construction_status = models.TextField(default='',null=True)
    status = models.TextField(default='',null=True)
    furnished = models.TextField(default='',null=True)
    security_deposit = models.BigIntegerField(default=0)
    rent_property = models.TextField(default='',null=True)
    rent_escalation_period = models.TextField(default='',null=True)
    rent_priority_comment = models.TextField(default='',null=True)
    size = models.BigIntegerField(default=0)
    carpet_area = models.BigIntegerField(default=0)
    type = models.TextField(default='',null=True)
    builder = models.TextField(default='',null=True)
    floor = models.IntegerField(default=0)
    total_floor = models.IntegerField(default=0)
    facing = models.TextField(default='',null=True)
    possession_type = models.TextField(default='',null=True)
    is_rented = models.BooleanField(default=False)
    rent = models.CharField(max_length=50, default='',null=True)
    cost = models.BigIntegerField(default=0)
    extra_charge = models.BigIntegerField(default=0)
    lease_time = models.CharField(max_length=20, default='',null=True)
    lease_completed = models.BooleanField(default=False)
    lease_balance = models.BigIntegerField(default=0)
    rent_escalation = models.TextField(default='',null=True)
    rent_to = models.CharField(max_length=50, default='',null=True)
    maintenance = models.CharField(max_length=50, default='',null=True)
    registry = models.CharField(max_length=100, default='',null=True)
    transfer_charge = models.BigIntegerField(default=0)
    gst = models.BigIntegerField(default=0)
    profit_sharing = models.BigIntegerField(default=0)
    roi = models.TextField(default='',null=True)
    profile_pic = models.ImageField(upload_to="projects/profile_pic/", blank=True, null=True)
    shop_for = models.TextField(default='',null=True)
    posted_by = models.TextField(default='',null=True)
    possession_status = models.BooleanField(default=False)
    possession_date = models.DateTimeField(null=True, blank=True)
    is_corner_plot = models.BooleanField(default=False)
    hidden_notes = models.FileField(upload_to="projects/hidden_notes", blank=True, null=True)
    lock_in = models.TextField(default='',null=True)
    power_breakup_rate = models.CharField(max_length=50, default='',null=True)
    road_size = models.CharField(max_length=100, default='')
    publisher = models.ForeignKey(Publisher, related_name='publisher', on_delete=models.CASCADE)
    meta_desc = models.TextField(default='',null=True)
    meta_key = models.CharField(max_length=200, default='',null=True)
    is_distress = models.BooleanField(default=False)
    reason_distress = models.CharField(max_length=100, default='',null=True)
    cost_distress = models.CharField(max_length=50, default='',null=True)
    recommended = models.BooleanField(default=False)
    plot_size = models.CharField(max_length=50, default='',null=True)
    construction_age = models.CharField(max_length=200, default='',null=True)
    code = models.CharField(max_length=50, default='',null=True)
    listing_date = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(max_length=200, default='',null=True)
    def __str__(self):
        return self.name
class Picture(models.Model):
    project_name = models.ForeignKey(Project,related_name="Pictuer", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/pictures/')

    def __str__(self):
        return f'Image for {self.project_name.name}'