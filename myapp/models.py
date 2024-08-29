from django.db import models
from api.models import Project,Location
from django.utils import timezone
import random
from django.core.validators import RegexValidator

class posts(models.Model): 
    name=models.CharField(max_length=50,null=True,blank=True)
    title=models.CharField(max_length=200,null=True,blank=True)
    comments=models.TextField(null=True,blank=True)
    image= models.FileField(upload_to="posts/image/", blank=True, null=True)
    pdf= models.FileField(upload_to="posts/pdf/", blank=True, null=True)
    post_date=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    
class shareholderPattern(models.Model):
    year=models.CharField(max_length=10,default='')
    month=models.CharField(max_length=25,default='')
    pdf=models.FileField(upload_to="shareholderPattern/",blank=True,null='',default='')
    
class compliance(models.Model):
    fy=models.CharField(max_length=15,default='')
    comp_type=models.CharField(max_length=50,null=True,default='')
    quarter=models.CharField(max_length=25,default='')
    description=models.CharField(max_length=200,null=True,default='')
    pdf=models.FileField(upload_to='compliance/',blank=True,null=True)

class projectEnquary(models.Model):
    firstName =models.CharField(max_length=50,default='')
    lastName =models.CharField(max_length=50,default='')
    email =models.CharField(max_length=50,default='')
    country =models.CharField(max_length=50,default='')
    cityName =models.CharField(max_length=50,default='')
    mobile =models.CharField(max_length=50,default='')
    projectName =models.CharField(max_length=50,default='')
    created_at=models.DateTimeField(auto_now=True,null=True)
    
class projectTable(models.Model):
    project=models.ForeignKey(Project,related_name="project",on_delete=models.CASCADE)
    price=models.CharField(max_length=50,default='')
    locality=models.CharField(max_length=50,default='')
    topology=models.CharField(max_length=50,default='')
    neighbourhood=models.CharField(max_length=100,default='Best Location in Your City')
    master_plan=models.FileField(upload_to="master_plans/",blank=True,null=True)
    unit_plan=models.FileField(upload_to="unit_plans/",blank=True,null=True)
    image=models.FileField(upload_to="project_image/")
    image2=models.FileField(upload_to="project_image2/",blank=True,null=True)
    image3=models.FileField(upload_to="project_image3/",blank=True,null=True)
    image4=models.FileField(upload_to="project_image4/",blank=True,null=True)
    

class schedulOn(models.Model):
    firstName =models.CharField(max_length=50,default='')
    lastName =models.CharField(max_length=50,default='')
    email =models.CharField(max_length=50,default='')
    country =models.CharField(max_length=50,default='')
    mobile =models.CharField(max_length=50,default='')
    schedule_data=models.CharField(max_length=30,default='')
    schedule_time=models.CharField(max_length=15,default='')
    projectName =models.CharField(max_length=50,default='')
    created_at=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return self.firstName
    
class Callback(models.Model):
    name = models.CharField(max_length=25,default='')
    country = models.CharField(max_length=50,default='')
    mobile = models.CharField(max_length=20,default='')
    email = models.EmailField(max_length=100,default='')
    confirm = models.BooleanField()
    created_at=models.DateTimeField(auto_now=True,null=True)
    def __str__(self):
        return f" Mobile {self.mobile} Name {self.name}"
    
class amenities(models.Model):
    project=models.ForeignKey(Project,related_name='amenities_set',on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='amenities/')
    def __str__(self):
        return f" Project {self.project.name} Amenties {self.name}"
    
class customer(models.Model):
    name = models.CharField(max_length=25)
    mobile = models.CharField(
        max_length=18,
        unique=True,
        null=True,
        blank=True,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid mobile number.')]
    )
    email = models.EmailField(
        unique=True,
        null=True,
        blank=True
    )
    countryName=models.CharField(max_length=50,null=True,blank=True)
    address = models.TextField(null=True,blank=True)
    password = models.CharField(max_length=8,null=True,blank=True)  # Ensure this is handled securely
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class OTP(models.Model):
    user = models.ForeignKey(customer, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def is_valid(self):
        # OTP is valid for 5 minutes
        return self.created_at >= timezone.now() - timezone.timedelta(minutes=5)
    
    @staticmethod
    def generate_otp():
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])
    
class chatboatData(models.Model):
    name=models.CharField(max_length=25)
    mobile=models.CharField(max_length=15)
    email=models.EmailField(max_length=50)
    created_at=models.DateTimeField(auto_now=True)
    
class sitevisiter(models.Model):
    mobile=models.CharField(max_length=20,default="Unknown")
    name=models.CharField(max_length=20,null=True,blank=True,default="Unknown")
    csrftoken=models.CharField(max_length=100,null=True,blank=True,default="")
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f" Mobile {self.mobile} Name {self.name}"
    
class membershipOffer(models.Model):
    type=models.CharField(max_length=150)
    offerPer=models.BigIntegerField()
    price=models.BigIntegerField()
    other=models.CharField(max_length=200)
    validTill=models.DateTimeField()
    image=models.FileField(upload_to='offerImage/')
    created_at=models.DateTimeField(auto_now=True)
    
class customerLead(models.Model):
    customer=models.ForeignKey(customer,on_delete=models.CASCADE)
    project=models.CharField(max_length=10)
    units=models.BigIntegerField()
    email=models.CharField(max_length=150)
    mobile=models.CharField(max_length=20)
    created_at=models.DateTimeField(auto_now=True)
    
class blog(models.Model):
    type=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=150)
    image=models.FileField(upload_to='blogs/',blank=True,null=True)
    distcription=models.TextField()
    view=models.BigIntegerField()
    created_at=models.DateTimeField(auto_now=True)

class blog_post(models.Model):
    type=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=150)
    image=models.FileField(upload_to='blogs/',blank=True,null=True)
    distcription=models.TextField()
    view=models.BigIntegerField()
    created_at=models.DateTimeField(auto_now=True)


class searchHistory(models.Model):
    user = models.ForeignKey(sitevisiter, blank=True, null=True, default="Unknown", on_delete=models.SET_NULL)
    searches=models.CharField(max_length=200, null=True,blank=True,default="None")
    url=models.CharField(max_length=200, null=True,blank=True,default="None")
    created_at=models.DateTimeField(auto_now=True)
    
class projectCallus(models.Model):
    name=models.CharField(max_length=50,blank=True,null=True)
    countryName=models.CharField(max_length=50,blank=True,null=True)
    countryCode=models.CharField(max_length=10,blank=True,null=True)
    city=models.CharField(max_length=50,blank=True,null=True)
    mobile=models.BigIntegerField(blank=True,null=True)
    projectName=models.CharField(max_length=200,blank=True,null=True)
    created_at=models.DateTimeField(auto_now=True,blank=True,null=True)
    def __str__(self):
        return f" Mobile {self.mobile} Name {self.name}"





    


