# api/models.py

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import secrets


class APIKey(models.Model):
    key = models.CharField(max_length=40, unique=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = secrets.token_urlsafe(32)  # Generate a random API key
        super().save(*args, **kwargs)

    def __str__(self):
        return self.key





class Location(models.Model):
    country=models.CharField(max_length=50,null=True,blank=True, default="NA")
    state=models.CharField(max_length=50,null=True,blank=True, default="NA")
    dist=models.CharField(max_length=50,null=True,blank=True, default="NA")
    city = models.CharField(max_length=50)
    other = models.CharField(max_length=255,default="NA",null=True,blank=True)
    longitude = models.CharField(max_length=50,default="NA",null=True,blank=True)
    latitude = models.CharField(max_length=50,default="NA",null=True,blank=True)
    def __str__(self):
        return f'Location: {self.city} in {self.state}'

class Publisher(models.Model):
    is_active = models.BooleanField(default=True)
    listing = models.BigAutoField(primary_key=True)
    state = models.CharField(max_length=255,default="NA")
    city = models.CharField(max_length=255,default="NA")
    department = models.CharField(max_length=255,default="NA")
    designation = models.CharField(max_length=255,default="NA")
    role = models.CharField(max_length=255,default="NA")
    name = models.CharField(max_length=255,default="NA")
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20,default="NA")
    password = models.CharField(max_length=50,default="NA")
    address = models.TextField(default="NA")
    created_on = models.DateTimeField(default=timezone.now)
    pub_id = models.CharField(max_length=255,default="NA")
    listing_date = models.DateTimeField(null=True, blank=True,default="NA")
    plan_id = models.CharField(max_length=50,default="NA")
    
    def __str__(self):
        return f'Publisher: {self.name}'

class Gallery(models.Model):
    publisher = models.ForeignKey(Publisher, related_name='galleries', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='projects/gallery/')
    
    def __str__(self):
        return f'Gallery Image for {self.publisher.name}'

class Project(models.Model):
    PROP_CHOICES = [
        ('Commercial', 'Commercial'),
        ('Residential', 'Residential'),
    ]
    PROP_STATUS=[
        ("Upcoming","Upcoming"),
        ("Pending","Pending"),
        ("New Launches","New Launches"),
        ("Other","Other")
    ]
    name = models.CharField(max_length=100)
    description = models.TextField(default="NA",null=True)
    picture = models.FileField(upload_to="projects/pictures/", blank=True, null=True)
    view = models.BigIntegerField(default=0)
    is_verified = models.BooleanField(default=False)
    is_for_rent = models.BooleanField(default=False)
    title = models.TextField(default="NA",null=True)
    location = models.ForeignKey(Location, related_name="location", on_delete=models.CASCADE)
    sub_area = models.CharField(max_length=50)
    property_type = models.CharField(max_length=100, choices=PROP_CHOICES, default='Commercial')
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    amenities = models.TextField(default="NA",null=True)
    nearby = models.TextField(default="NA",null=True)
    expiration_date = models.DateTimeField(null=True, blank=True)
    construction_status = models.BooleanField(default=False)
    status = models.CharField(max_length=50,choices=PROP_STATUS,default="Complete")
    furnished = models.TextField(default="NA",null=True)
    security_deposit = models.BigIntegerField(default=0)
    rent_property = models.TextField(default="NA",null=True)
    rent_escalation_period = models.TextField(default="NA",null=True)
    rent_priority_comment = models.TextField(default="NA",null=True)
    size = models.BigIntegerField(default=0)
    carpet_area = models.BigIntegerField(default=0)
    type = models.TextField(default="NA",null=True)
    builder = models.TextField(default="NA",null=True)
    floor = models.IntegerField(default=0)
    total_floor = models.IntegerField(default=0)
    facing = models.TextField(default="NA",null=True)
    possession_type = models.TextField(default="NA",null=True)
    is_rented = models.BooleanField(default=False)
    rent = models.CharField(max_length=50, default="NA",null=True)
    cost = models.BigIntegerField(default=0)
    extra_charge = models.BigIntegerField(default=0)
    lease_time = models.CharField(max_length=20, default="NA",null=True)
    lease_completed = models.BooleanField(default=False)
    lease_balance = models.BigIntegerField(default=0)
    rent_escalation = models.TextField(default="NA",null=True)
    rent_to = models.CharField(max_length=50, default="NA",null=True)
    maintenance = models.CharField(max_length=50, default="NA",null=True)
    registry = models.CharField(max_length=100, default="NA",null=True)
    transfer_charge = models.BigIntegerField(default=0)
    gst = models.BigIntegerField(default=0)
    profit_sharing = models.BigIntegerField(default=0)
    roi = models.TextField(default="NA",null=True)
    profile_pic = models.ImageField(upload_to="projects/profile_pic/", blank=True, null=True)
    shop_for = models.TextField(default="NA",null=True)
    posted_by = models.TextField(default="NA",null=True)
    possession_status = models.BooleanField(default=False)
    possession_date = models.DateTimeField(null=True, blank=True)
    is_corner_plot = models.BooleanField(default=False)
    hidden_notes = models.FileField(upload_to="projects/hidden_notes", blank=True, null=True)
    lock_in = models.TextField(default="NA",null=True)
    power_breakup_rate = models.CharField(max_length=50, default="NA",null=True)
    road_size = models.CharField(max_length=100, default="NA")
    publisher = models.ForeignKey(Publisher, related_name='publisher', on_delete=models.CASCADE)
    meta_desc = models.TextField(default="NA",null=True)
    meta_key = models.CharField(max_length=200, default="NA",null=True)
    is_distress = models.BooleanField(default=False)
    reason_distress = models.CharField(max_length=100, default="NA",null=True)
    cost_distress = models.CharField(max_length=50, default="NA",null=True)
    recommended = models.BooleanField(default=False)
    plot_size = models.CharField(max_length=50, default="NA",null=True)
    construction_age = models.CharField(max_length=200, default="NA",null=True)
    code = models.CharField(max_length=50, default="NA",null=True)
    listing_date = models.DateTimeField(null=True, blank=True)
    slug = models.SlugField(max_length=200, default="NA",null=True)
    def __str__(self):
        return self.name
class Picture(models.Model):
    project_name = models.ForeignKey(Project,related_name="Pictuer", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='projects/pictures/')

    def __str__(self):
        return f'Image for {self.project_name.name}'
    
class History(models.Model):
    visiter = models.ForeignKey('myapp.sitevisiter', on_delete=models.CASCADE, null=True, blank=True)
    action = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    record_id = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.action} on record ID {self.record_id} at {self.timestamp}"

