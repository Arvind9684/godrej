# myapp/forms.py
from django import forms
from api.models import *
from django.apps import apps
from myapp.models import customer

class OTPForm(forms.Form):
    otp = forms.CharField(max_length=6, widget=forms.TextInput(attrs={'placeholder': 'Enter OTP'}))
    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'description', 'view', 'is_verified', 'is_for_rent', 'title', 'location',
            'sub_area', 'property_type', 'category', 'sub_category', 'website', 'amenities',
            'nearby', 'construction_status', 'status', 'furnished', 'security_deposit', 'rent_property',
            'rent_escalation_period', 'rent_priority_comment', 'size', 'carpet_area', 'type', 'builder',
            'floor', 'total_floor', 'facing', 'possession_type', 'is_rented', 'rent', 'cost',
            'extra_charge', 'lease_time', 'lease_completed', 'lease_balance', 'rent_escalation',
            'rent_to', 'maintenance', 'registry', 'transfer_charge', 'gst', 'profit_sharing', 'roi',
            'profile_pic', 'shop_for', 'posted_by', 'possession_status', 'is_corner_plot', 'hidden_notes',
            'lock_in', 'power_breakup_rate', 'road_size', 'publisher', 'meta_desc', 'meta_key', 'is_distress',
            'reason_distress', 'cost_distress', 'recommended', 'plot_size', 'construction_age', 'code',
            'listing_date', 'slug'
        ]



def buildForm(name):
    # Define the DynamicForm class with the retrieved model
    class DynamicForm(forms.ModelForm):
        class Meta:
            model=None
            # Try to get the model from 'myapp' first, then from 'api'
            try:
                model = apps.get_model('myapp', name)
            except LookupError:
                model = apps.get_model('api', name)
            model = model
            fields = '__all__'

    return DynamicForm

class TextToAudioForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Enter text')
    
class CustomerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = [
            "name",
            "mobile",
            "email",
            "countryName",
            "address",
            "password",
        ]
        widgets = {
            'password': forms.PasswordInput(),
        }