from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from django.core.exceptions import PermissionDenied
import requests
from django.http import JsonResponse
from django.core.paginator import Paginator
import pandas as pd
import numpy as np
from django.middleware.csrf import get_token
from django.db.models import Sum
import datetime as dt
from django.http import FileResponse
from django.forms import modelform_factory
from myapp.models import (shareholderPattern,compliance,projectEnquary,projectTable,Callback,amenities,customer,
                          OTP,posts,chatboatData,sitevisiter,schedulOn,membershipOffer,customerLead,blog,blog_post,
                          searchHistory,projectCallus)
from myapp.utils import get_project_list,sendOtp
import ast,shutil,random,os
from django.http import HttpResponseRedirect
from api.models import (Project,Publisher,History,Location)
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseNotFound,HttpResponse
from django.apps import apps
from django.core.files.storage import FileSystemStorage
from django.utils.dateparse import parse_datetime
from django.utils.dateparse import parse_date
from django.contrib import messages
from myapp.forms import ProjectForm,buildForm,TextToAudioForm,CustomerForm
from gtts import gTTS
from pdf2image import convert_from_path
import matplotlib.pyplot as plt
from django.conf import settings
from pdfminer.high_level import extract_text_to_fp
from io import StringIO,BytesIO
from django.views.decorators.csrf import csrf_exempt
import json
from gmplot import gmplot
from django.conf import settings



def copy_pdf_to_other_location(post, destination_dir):
    # Ensure the destination directory exists
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Get the current path of the PDF file
    pdf_path = post.pdf.path

    # Define the new path for the copied file
    # Extract the filename from the original path
    filename = os.path.basename(pdf_path)
    new_path = os.path.join(destination_dir, filename)

    # Copy the file to the new location
    shutil.copy(pdf_path, new_path)

    return new_path


def index(request):
    # Read the CSV files
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    # print(city_df)
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_list = get_project_list()
    project_field_names = [field.name for field in Project._meta.get_fields() if not field.many_to_one]
    # Retrieve all Project records
    projects_data = Project.objects.all().values(*project_field_names)
    zipped_projects = []
    for project in projects_data:
        zipped_project = dict(zip(project_field_names, [project[field] for field in project_field_names]))
        zipped_projects.append(zipped_project)
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    # print(projects_df.columns)
    context = {
        "project_list": project_list,
        "country_flag_df": country_flag_df,
        'last_url_word': last_url_word,
        'zipped_projects':zipped_projects,
        'city':city,
    }
    return render(request, "index.html", context)
    # return render(request, "error.html", context)

def project(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    # print(city_df)
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_list = get_project_list()
    # print(project_list)  # For debugging
    
    #--------------------------------------------------------------------------------
    # Number of items per page
    one_page = 9
    paginator = Paginator(project_list, one_page)
    
    # Get the current page number
    page_number = request.GET.get('page')
    
    # Get the page object for the current page
    page_obj = paginator.get_page(page_number)
    
    # If the page number is 1 or None, slice the data for the first page
    if page_number == "1" or page_number is None:
        project_list = project_list[:one_page]
    else:
        start_index = one_page * (int(page_number) - 1)
        end_index = one_page * int(page_number)
        project_list = project_list[start_index:end_index]
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(project_list)
    city=projects_df['city'].unique()
    context={
        'page_obj': page_obj,
        "project_list":project_list,
        "country_flag_df":country_flag_df,
        'last_url_word':last_url_word,
        'city':city,
    }

    return render(request,"project.html",context)

def hometally(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_list = get_project_list()
    # print(project_list)  # For debugging
    project_df = pd.DataFrame(project_list) 
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    
    context={
        'project_list':project_list,
        'full_url':full_url,
        'last_url_word':last_url_word,
        'country_flag_df':country_flag_df,
        'city':city,
    }
    return render(request,"hometally.html",context)

def aboutus(request):
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'aboutus':"active",
        'full_url': full_url,
        'last_url_word': last_url_word,
        'city':city,
    }
    return render(request,"aboutus.html",context)

def management(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'country_flag_df':country_flag_df,
        'management':'active',
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'city':city,
    }
    return render(request,"management.html",context)

def sustatnability(request):
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'country_flag_df':country_flag_df,
        'sustatnability':'active',
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'ctiy':city,
    }
    return render(request,"sustatnability.html",context)

def design(request):
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'design':'active',
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'country_flag_df':country_flag_df,
        'city':city,
    }
    return render(request,"design.html",context)

def residential(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_list = get_project_list()
    # print(project_list)  # For debugging
    project_df = pd.DataFrame(project_list) 
    project = project_df[project_df['property_type'] == 'Residential']

    # Convert DataFrame to a list of dictionaries
    project_list = project.to_dict(orient='records')
    #--------------------------------------------------------------------------------
    # Number of items per page
    one_page = 9
    paginator = Paginator(project, one_page)
    
    # Get the current page number
    page_number = request.GET.get('page')
    
    # Get the page object for the current page
    page_obj = paginator.get_page(page_number)
    
    # If the page number is 1 or None, slice the data for the first page
    if page_number == "1" or page_number is None:
        project = project[:one_page]
    else:
        start_index = one_page * (int(page_number) - 1)
        end_index = one_page * int(page_number)
        project = project[start_index:end_index]
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'page_obj': page_obj,
        "project":project,
        "country_flag_df":country_flag_df,
        'project_list':project_list,
        'last_url_word':last_url_word,
        'city':city,
    }
    return render(request,"project.html",context)

def commercial(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_list = get_project_list()
    # print(project_list)  # For debugging
    project_df = pd.DataFrame(project_list) 
    project = project_df[project_df['property_type'] == 'Commercial']

    # Convert DataFrame to a list of dictionaries
    project_list = project.to_dict(orient='records')
    #--------------------------------------------------------------------------------
    # Number of items per page
    one_page = 9
    paginator = Paginator(project, one_page)
    
    # Get the current page number
    page_number = request.GET.get('page')
    
    # Get the page object for the current page
    page_obj = paginator.get_page(page_number)
    
    # If the page number is 1 or None, slice the data for the first page
    if page_number == "1" or page_number is None:
        project = project[:one_page]
    else:
        start_index = one_page * (int(page_number) - 1)
        end_index = one_page * int(page_number)
        project = project[start_index:end_index]
    project.to_csv("myapp/static/project.csv", index=False)
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'page_obj': page_obj,
        "project":project,
        "country_flag_df":country_flag_df,
        'project_list':project_list,
        'last_url_word':last_url_word,
        'city':city,
    }
    return render(request,"project.html",context)

def finance(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_list = get_project_list()
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'finance':'active',
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'country_flag_df':country_flag_df,
        'city':city,
    }
    return render(request,'finance.html',context)

def investorInform(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_list = get_project_list()
    shareholderPattern_data = shareholderPattern.objects.all().values()
    
    # Step 2: Convert the QuerySet to a list of dictionaries
    shareholderPattern_list = list(shareholderPattern_data)

    # Step 3: Create a Pandas DataFrame
    shareholderPattern_df = pd.DataFrame(shareholderPattern_list)
    
    if not shareholderPattern_df.empty:
        years = shareholderPattern_df['year'].unique()
    else:
        years = []  # or some other default value

    
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'country_flag_df':country_flag_df,
        'investorInform':'active',
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'years':years,
        'shareholderPattern_df':shareholderPattern_df,
        'country_flag_df':country_flag_df,
        'city':city,
    }
    return render(request,'investorInform.html',context)

def governanceLeasership(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'governanceLeasership':'active',
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'country_flag_df':country_flag_df,
        'city':city,
    }
    return render(request,'governanceLeasership.html',context)

def compliances(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    
    # Fetch all compliance objects
    compliance_data = compliance.objects.all().values('fy','comp_type','quarter','description', 'pdf')

    # Convert to DataFrame
    compliance_df = pd.DataFrame(list(compliance_data))
    compliance_df = compliance_df[compliance_df["comp_type"]=="regulations"]
    
    fy_unique=compliance_df['fy'].unique()

    # Initialize first and second as empty lists
    first_list = []
    second_list = []
    third_list = []
    fourth_list = []

    # Check if the 'quarter' column is present
    if 'quarter' in compliance_df.columns:
        first = compliance_df[compliance_df["quarter"] == "first"]
        second = compliance_df[compliance_df["quarter"] == "second"]
        third = compliance_df[compliance_df["quarter"] == "third"]
        fourth = compliance_df[compliance_df["quarter"] == "fourth"]

        # Convert the filtered DataFrame back to a list of dictionaries if not empty
        if not first.empty:
            first_list = first.to_dict('records')
        if not second.empty:
            second_list = second.to_dict('records')
        if not third.empty:
            third_list = second.to_dict('records')
        if not fourth.empty:
            fourth_list = second.to_dict('records')
    project_list = get_project_list()
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'regulations':"active",
        'first':first_list,
        'second':second_list,
        'third':third_list,
        'fourth':fourth_list,
        'fy_unique':fy_unique,
        'country_flag_df':country_flag_df,
        'city':city,
    }
    return render(request,'compliances.html',context)

def csr(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    # Fetch all compliance objects
    compliance_data = compliance.objects.all().values('fy', 'comp_type', 'quarter', 'description', 'pdf')

    # Convert to DataFrame
    compliance_df = pd.DataFrame(list(compliance_data))

    # Filter for comp_type == "dividend"
    compliance_df = compliance_df[compliance_df["comp_type"] == "csr-committee"]

    # Convert the filtered DataFrame to a dictionary for the template
    csr_df = compliance_df.to_dict(orient='records')

    # Get unique fiscal years
    fy_unique = compliance_df['fy'].unique()
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()

    context={
        'country_flag_df':country_flag_df,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'csr':"active",
        'csr_df':csr_df,
        'fy_unique':fy_unique,
        'project_list':project_list,
        'city':city,
    }
    return render(request,'csr.html',context)

def discloser(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'full_url': full_url,
        'last_url_word': last_url_word,
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'city':city,
    }
    return render(request,'discloser.html',context)

def ballot(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    # Fetch all compliance objects
    compliance_data = compliance.objects.all().values('fy','comp_type','quarter','description', 'pdf')

    # Convert to DataFrame
    compliance_df = pd.DataFrame(list(compliance_data))
    compliance_df = compliance_df[compliance_df["comp_type"]=="ballot"]
    
    fy_unique=compliance_df['fy'].unique()

    # Initialize first and second as empty lists
    first_list = []
    second_list = []
    third_list = []
    fourth_list = []

    # Check if the 'quarter' column is present
    if 'quarter' in compliance_df.columns:
        first = compliance_df[compliance_df["quarter"] == "first"]
        second = compliance_df[compliance_df["quarter"] == "second"]
        third = compliance_df[compliance_df["quarter"] == "third"]
        fourth = compliance_df[compliance_df["quarter"] == "fourth"]

        # Convert the filtered DataFrame back to a list of dictionaries if not empty
        if not first.empty:
            first_list = first.to_dict('records')
        if not second.empty:
            second_list = second.to_dict('records')
        if not third.empty:
            third_list = second.to_dict('records')
        if not fourth.empty:
            fourth_list = second.to_dict('records')

    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()

    context={
        'country_flag_df':country_flag_df,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'ballot':"active",
        'first':first_list,
        'second':second_list,
        'third':third_list,
        'fourth':fourth_list,
        'fy_unique':fy_unique,
        'project_list':project_list,
        'city':city,
    }
    return render(request,'compliances.html',context)

def dividend(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    # Fetch all compliance objects
    compliance_data = compliance.objects.all().values('fy', 'comp_type', 'quarter', 'description', 'pdf')

    # Convert to DataFrame
    compliance_df = pd.DataFrame(list(compliance_data))

    # Filter for comp_type == "dividend"
    compliance_df = compliance_df[compliance_df["comp_type"] == "dividend"]

    # Convert the filtered DataFrame to a dictionary for the template
    dividend_df = compliance_df.to_dict(orient='records')

    # Get unique fiscal years
    fy_unique = compliance_df['fy'].unique()
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()

    context={
        'country_flag_df':country_flag_df,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'dividend':"active",
        'dividend_df':dividend_df,
        'fy_unique':fy_unique,
        'porject_list':project_list,
        'city':city,
    }
    return render(request,'compliances.html',context)

def esop(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    # Fetch all compliance objects
    compliance_data = compliance.objects.all().values('fy', 'comp_type', 'quarter', 'description', 'pdf')

    # Convert to DataFrame
    compliance_df = pd.DataFrame(list(compliance_data))

    # Filter for comp_type == "dividend"
    compliance_df = compliance_df[compliance_df["comp_type"] == "esop"]

    # Convert the filtered DataFrame to a dictionary for the template
    esop_df = compliance_df.to_dict(orient='records')
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    
    context={
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'esop':"active",
        'esop_df':esop_df,
        'city':city,
        
    }
    return render(request,'compliances.html',context)

def qip(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()

    context={
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'qip':"active",
        'city':city,
    }
    return render(request,'compliances.html',context)

def scheme(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    # Fetch all compliance objects
    compliance_data = compliance.objects.all().values('fy', 'comp_type', 'quarter', 'description', 'pdf')

    # Convert to DataFrame
    compliance_df = pd.DataFrame(list(compliance_data))

    # Filter for comp_type == "dividend"
    compliance_df = compliance_df[compliance_df["comp_type"] == "scheme"]

    # Convert the filtered DataFrame to a dictionary for the template
    scheme_df = compliance_df.to_dict(orient='records')
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()

    
    context={
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'scheme':"active",
        'scheme_df':scheme_df,
        'city':city,
        
    }
    return render(request,'compliances.html',context)
  

def credit(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    # Fetch all compliance objects
    compliance_data = compliance.objects.all().values('fy', 'comp_type', 'quarter', 'description', 'pdf')

    # Convert to DataFrame
    compliance_df = pd.DataFrame(list(compliance_data))

    # Filter for comp_type == "dividend"
    compliance_df = compliance_df[compliance_df["comp_type"] == "credit"]

    # Convert the filtered DataFrame to a dictionary for the template
    credit_df = compliance_df.to_dict(orient='records')
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    
    context={
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'credit':"active",
        'credit_df':credit_df,
        'city':city,
        
    }
    return render(request,'compliances.html',context)


def procedure(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'procedure':"active",
        'city':city,
    }
    return render(request,'compliances.html',context)
 

def egm(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    # Fetch all compliance objects
    compliance_data = compliance.objects.all().values('fy', 'comp_type', 'quarter', 'description', 'pdf')

    # Convert to DataFrame
    compliance_df = pd.DataFrame(list(compliance_data))

    # Filter for comp_type == "dividend"
    compliance_df = compliance_df[compliance_df["comp_type"] == "egm"]

    # Convert the filtered DataFrame to a dictionary for the template
    egm_df = compliance_df.to_dict(orient='records')

    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'egm':"active",
        'egm_df':egm_df,
        'city':city,
        
    }
    return render(request,'compliances.html',context)
     
def annual(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    # Fetch all compliance objects
    compliance_data = compliance.objects.all().values('fy', 'comp_type', 'quarter', 'description', 'pdf')

    # Convert to DataFrame
    compliance_df = pd.DataFrame(list(compliance_data))

    # Filter for comp_type == "dividend"
    compliance_df = compliance_df[compliance_df["comp_type"] == "csr-annual"]

    # Convert the filtered DataFrame to a dictionary for the template
    annual_df = compliance_df.to_dict(orient='records')

    # Get unique fiscal years
    fy_unique = compliance_df['fy'].unique()
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'annual':"active",
        'annual_df':annual_df,
        'fy_unique':fy_unique,
        'city':city,
    }
    return render(request,'csr.html',context)

def commission(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    # Fetch all compliance objects
    compliance_data = compliance.objects.all().values('fy', 'comp_type', 'quarter', 'description', 'pdf')

    # Convert to DataFrame
    compliance_df = pd.DataFrame(list(compliance_data))

    # Filter for comp_type == "dividend"
    compliance_df = compliance_df[compliance_df["comp_type"] == "commission"]

    # Convert the filtered DataFrame to a dictionary for the template
    commission_df = compliance_df.to_dict(orient='records')

    # Get unique fiscal years
    fy_unique = compliance_df['fy'].unique()
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()

    context={
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url': full_url,
        'last_url_word': last_url_word,
        'commission':"active",
        'commission_df':commission_df,
        'fy_unique':fy_unique,
        'city':city,
    }
    return render(request,'csr.html',context)

def news(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        "news":"active",
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url':full_url,
        'last_url_word':last_url_word,
        'image_text':"In the News",
        'image_path':"../media/image/mediabackground.jpg",
        'city':city,
        
    }
    return render(request,'media.html',context)

def pressreleas(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        "pressreleas":"active",
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url':full_url,
        'last_url_word':last_url_word,
        'image_text':"",
        'image_path':"../media/image/pressrelease.jpg",
        'city':city
        
    }
    return render(request,'media.html',context)

def mediagallery(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(project_list)
    city=projects_df['city'].unique()
    context={
        "mediagallery":"active",
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url':full_url,
        'last_url_word':last_url_word,
        'image_text':"Media",
        'image_path':"../media/image/mediagallery.jpg",
        'city':city,
        
    }
    return render(request,'media.html',context)
    
def legalinformation(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(project_list)
    city=projects_df['city'].unique()
    context={
        "legalinformation":"active",
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url':full_url,
        'last_url_word':last_url_word,
        'city':city,
        
    }
    return render(request,'nricorner.html',context)

def loanfornri(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(project_list)
    city=projects_df['city'].unique()
    context={
        "loanfornri":"active",
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url':full_url,
        'last_url_word':last_url_word,
        'city':city,
        
    }
    return render(request,'nricorner.html',context)
 
def nrifaq(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(project_list)
    city=projects_df['city'].unique()
    
    context={
        "nrifaq":"active",
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url':full_url,
        'last_url_word':last_url_word,
        'city':city,
        
    }
    return render(request,'nricorner.html',context)

def internationaloffice(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    projects_df=pd.DataFrame(project_list)
    city=projects_df['city'].unique()
    
    context={
        "internationaloffice":"active",
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url':full_url,
        'last_url_word':last_url_word,
        'city':city,
        
    }
    return render(request,'nricorner.html',context)

def enqurenow(request):
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    if request.method=="POST":
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        email=request.POST.get('email')
        country=request.POST.get('countryName')
        cityName=request.POST.get('city')
        mobile=request.POST.get('mobile')
        projectName=request.POST.get('project')
        ins=projectEnquary(
            firstName = firstName,
            lastName = lastName,
            email = email,
            country = country,
            cityName = cityName,
            mobile = mobile,
            projectName = projectName
        )
        ins.save()
        return redirect(last_url_word)

    # Read the CSV files
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    projects_df=pd.DataFrame(project_list)
    city=projects_df['city'].unique()
    context={
        "enqurenow":"active",
        "projects":project_list,
        'full_url':full_url,
        'last_url_word':last_url_word,
        "country_flag_df":country_flag_df,
        'city':city,
        
    }
    return render(request,'nricorner.html',context)

def blogs(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    project_list = get_project_list()
    sliderImage=["design.webp","design.png","design.jpg","design2.png","design2.webp","design3.png","aboutusBackground.png","medianews.jpg"]
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    last_blog=blog.objects.last()
    blogs_data=blog.objects.all()
    # Retrieve the last three blog entries
    last_three_blogs = blog.objects.all().order_by('-id')[:3]
    blog_post_data=blog_post.objects.all()
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context={
        "enqurenow":"active",
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'full_url':full_url,
        'last_url_word':last_url_word,
        'sliderImage':sliderImage,
        'last_blog':last_blog,
        'blogs_data':blogs_data,
        'last_three_blogs':last_three_blogs,
        'blog_post_data':blog_post_data,
        'city':city,
    }
    return render(request,'blogs.html',context)
def ambessador(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    context={
        "country_flag_df":country_flag_df,
    }
    return render(request,'ambessador/ambessador.html',context)

def project_enquiry(request):
    if request.method=="POST":
        firstName=request.POST.get('firstName')
        lastName=request.POST.get('lastName')
        email=request.POST.get('email')
        country=request.POST.get('countryName')
        cityName=request.POST.get('city')
        mobile=request.POST.get('mobile')
        projectName=request.POST.get('project')
        ins=projectEnquary(
            firstName = firstName,
            lastName = lastName,
            email = email,
            country = country,
            cityName = cityName,
            mobile = mobile,
            projectName = projectName
        )
        ins.save()
        return redirect('project')

def chunk_list(lst, chunk_size):
    for i in range(0, len(lst), chunk_size):
        yield lst[i:i + chunk_size]
def projectview(request,id):
    # Read the CSV files
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_list = get_project_list()
    # print(project_list)  # For debugging
    
    project_df = pd.DataFrame(project_list)
    project_df2 = project_df[project_df['id']==id]
    project_name = project_df2.iloc[0]['name']
    amenities_data = amenities.objects.filter(project__name=project_name)
    # print("Amenities : ",amenities_data)
    project_list2 = project_df2.to_dict(orient='records')
    city=project_df['city'].unique()
    
    context={
        "project_list":project_list,
        "country_flag_df":country_flag_df,
        'last_url_word':last_url_word,
        'project_list2':project_list2,
        'amenities_data':amenities_data,
        "city":city,
    }
    return render(request,'projectview.html',context)

from django.http import HttpResponseRedirect
from .models import Callback  # Make sure to import your Callback model

def callback(request, last_url_word):
    if request.method == "POST":
        name = request.POST.get('name')
        country = request.POST.get('country')  # No need for ast.literal_eval
        countrycode = request.POST.get('countrycode')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        confirm = request.POST.get('confirm') == 'on'  # Convert "on" to True

        # Concatenate country code and mobile number
        mobile = f"{countrycode} {mobile}"

        # Create and save the callback instance
        ins = Callback(
            name=name,
            country=country,  # Directly use the country string
            mobile=mobile,
            email=email,
            confirm=confirm
        )
        ins.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def real_estate_terms(request,msg):
    # print(msg)
    # Read the CSV files
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_list = get_project_list()
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    if msg=='termcondition':
        context={
            'country_flag_df':country_flag_df,
            'project_list':project_list,
            'termcondition':True,
            'city':city,
        }
        return render(request,"realtermcondition.html",context)
    elif msg=='onlineresearch':
        context={
            'country_flag_df':country_flag_df,
            'project_list':project_list,
            'onlineresearch':True,
            'city':city,
        }
        return render(request,"realtermcondition.html",context)
    elif msg=='rightproperty':
        context={
            'country_flag_df':country_flag_df,
            'project_list':project_list,
            'rightproperty':True,
            'city':city,
        }
        return render(request,"realtermcondition.html",context)
        
    else:
        return redirect(msg)
    
    
def reachus(request):
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_list = get_project_list()
    projects_df=pd.DataFrame(project_list)
    city=projects_df['city'].unique()
    context={
        'country_flag_df':country_flag_df,
        'project_list':project_list,
        'city':city,
    }
    return render(request,'reachus.html',context)

def sendEmail(request):
    if request.method == "POST":
        email = request.POST.get('email')
        countryName = request.POST.get('countryName')
        
        try:
            user = customer.objects.get(email=email)
            otptable, created = OTP.objects.get_or_create(user=user)
            
            if not created:
                # If OTP already exists, check if it is still valid
                if otptable.is_valid():
                    otp = otptable.otp
                else:
                    # Generate a new OTP if the existing one is expired
                    otp = OTP.generate_otp()
                    otptable.otp = otp
                    otptable.created_at = timezone.now()
                    otptable.save()
            else:
                # Generate a new OTP for a new entry
                otp = OTP.generate_otp()
                otptable.otp = otp
                otptable.save()
            
            # Send the OTP via email
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp}',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            context={
                "msg":f'OTP sent to {email}',
                'email':email,
            }
            return render(request,'ambessador/verfyotp.html',context)
        
        except customer.DoesNotExist:
            ins=customer(email=email,countryName=countryName)
            ins.save()
            user = customer.objects.get(email=email)
            otptable, created = OTP.objects.get_or_create(user=user)
            
            if not created:
                # If OTP already exists, check if it is still valid
                if otptable.is_valid():
                    otp = otptable.otp
                else:
                    # Generate a new OTP if the existing one is expired
                    otp = OTP.generate_otp()
                    otptable.otp = otp
                    otptable.created_at = timezone.now()
                    otptable.save()
            else:
                # Generate a new OTP for a new entry
                otp = OTP.generate_otp()
                otptable.otp = otp
                otptable.save()
            
            # Send the OTP via email
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp}',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            
            context={
                "msg":f'OTP sent to {email}',
                'email':email,
            }
            return render(request,'ambessador/verfyotp.html',context)
    return redirect("/")

def sendMobile(request):
    if request.method=="POST":
        email=request.POST.get('mobile')
        user=customer.objects.get(email=email)
        otp=OTP.objects.get(user=user)
        countryName=request.POST.get('countryName')
        context={
            "OTP":otp,
            'email':email,
        }
        return render(request,'ambessador/index.html',context)
def verifyotp(request):
    if request.method == "POST":
        email = request.POST.get('email')
        recOTP = request.POST.get('otp')
        try:
            user = customer.objects.get(email=email)
            otpTable = OTP.objects.filter(user=user).latest('created_at')
            otp = otpTable.otp
            
            if otp == recOTP and otpTable.is_valid():
                return redirect('ambessador/customer')
            else:
                context={
                    'error':"OTP did not match or has expired",
                    'email':email,
                }
                return render(request,'ambessador/verfyotp.html',context)
        
        except customer.DoesNotExist:
            return redirect('/')
        except OTP.DoesNotExist:
            return redirect('/')
    
    return render(request, 'ambessador/verfyotp.html')

def ambessador_customer(request):
    customer_data = customer.objects.last()
    request.session['customer_id']=customer_data.id

    if request.method == 'POST':
        if customer_data:
            customer_form = CustomerForm(request.POST, instance=customer_data)
        else:
            customer_form = CustomerForm(request.POST)
        
        if customer_form.is_valid():
            customer_form.save()  # This saves the data to the model
            return redirect('ambessador/units')  # Redirect to a success page or another view after saving
    else:
        if customer_data:
            customer_form = CustomerForm(instance=customer_data)
        else:
            customer_form = CustomerForm()

    context = {
        'customer_data': customer_data,
        'customerForm': customer_form,
        'customer': True,
    }
    return render(request, 'ambessador/customer.html', context)


def administrator(request):
    # अगर उपयोगकर्ता पहले से लॉगिन है, तो डैशबोर्ड पर रीडायरेक्ट करें
    if request.user.is_authenticated:
        return redirect('administrator_dashboard')
    # अन्यथा, लॉगिन पेज रेंडर करें
    return render(request, 'administrator/login.html')

def administratorlogin(request):
    # अगर उपयोगकर्ता पहले से लॉगिन है, तो डैशबोर्ड पर रीडायरेक्ट करें
    if request.user.is_authenticated:
        return redirect('administrator_dashboard')

    # लॉगिन फॉर्म को प्रोसेस करें
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('administrator_dashboard')  # सफल लॉगिन पर डैशबोर्ड पर रीडायरेक्ट करें
    
    # फॉर्म को वैध मानकर या पेज लोड के लिए लॉगिन पेज रेंडर करें
    form = AuthenticationForm()
    return render(request, 'administrator/login.html', {'form': form})

@login_required
def administrator_dashboard(request):
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_field_names = [field.name for field in Project._meta.get_fields() if not field.many_to_one]
    # Retrieve all Project records
    projects_data = Project.objects.all().values(*project_field_names)
    projects_df=pd.DataFrame(list(projects_data))
    # Get field names from the model
    schedulOn_field_names = [field.name for field in schedulOn._meta.get_fields() if not field.many_to_one]
    # Retrieve all records from schedulOn model with the selected fields
    schedulOn_data = schedulOn.objects.all().values(*schedulOn_field_names)
    # Convert QuerySet to DataFrame
    schedulOn_df = pd.DataFrame(list(schedulOn_data))
    # Group by 'projectName' and count occurrences
    schedulOn_group_df = schedulOn_df.groupby('projectName').size().reset_index(name='Count')
    # Print the grouped DataFrame
    #print(schedulOn_group_df)
    customerLead_field_name=[field.name for field in customerLead._meta.get_fields() if not field.many_to_one]
    customerLead_data=customerLead.objects.all().values(*customerLead_field_name)
    customerLead_df=pd.DataFrame(list(customerLead_data))
    # print("customerLead_df\n",customerLead_df)
    # Group by project and count the occurrences
    customerLead_group_df = customerLead_df.groupby('project').size().reset_index(name='Counts')

    # Convert 'project' column to integer type to match 'id' type in projects_df
    customerLead_group_df['project'] = customerLead_group_df['project'].astype(int)

    # Merge with the projects_df to get the project names
    customerLead_group_df = pd.merge(customerLead_group_df[["project", "Counts"]], projects_df[['id', 'name']], left_on='project', right_on='id', how='left')
    # print(customerLead_group_df)
    # Optionally, replace 'project' with 'name' if you want to keep project names instead of IDs
    customerLead_group_df['project'] = customerLead_group_df['name']
    customerLead_group_df.drop(columns=['name', 'id'], inplace=True)
    # Final DataFrame with project names and counts
    # print(customerLead_group_df)
    projectCallus_field_names = [field.name for field in projectCallus._meta.get_fields() if not field.many_to_one]
    projectCallus_data=projectCallus.objects.all().values(*projectCallus_field_names)
    projectCallus_df=pd.DataFrame(list(projectCallus_data))
    # print(projectCallus_df)
    # Group by 'projectName' and count the occurrences for each column
    projectCallus_group_df = projectCallus_df.groupby('projectName').count().reset_index()
    # Optionally, you can focus on a specific column if you want to count based on that
    projectCallus_group_df = projectCallus_df.groupby('projectName').size().reset_index(name='Count')
    # Print the result to see the grouped data
    # print("counts\n",projectCallus_group_df)
    projectEnquary_field_name=[field.name for field in projectEnquary._meta.get_fields() if not field.many_to_one]
    projectEnquary_data=projectEnquary.objects.all().values(*projectEnquary_field_name)
    projectEnquary_df=pd.DataFrame(list(projectEnquary_data))
    projectEnquary_group_df=projectEnquary_df.groupby("projectName").size().reset_index()
    
    context={
        "last_url_word":last_url_word,
        "property_count":projects_df["id"].count(),
        "cust_count":customer.objects.all().count(),
        "earning":projectTable.objects.aggregate(total_price=Sum('price'))['total_price'],
        "schedulOn_group_df":schedulOn_group_df,
        "chatboatData_count":chatboatData.objects.all().count(),
        "Callback_count":Callback.objects.all().count(),
        "sitevisiter_count":sitevisiter.objects.all().count(),
        'customerLead_group_df':customerLead_group_df,
        "projectCallus_group_df":projectCallus_group_df,
        "blogs_count":blog.objects.all().count(),
        "projectEnquary_group_df":projectEnquary_group_df,
    }
    
    return render(request, 'administrator/dashboard.html',context)

def custom_403_view(request, exception):
    return render(request, 'adminstrator/403.html', status=403)

def custom_404_view(request, exception):
    return render(request, 'administrator/404.html', status=404)
def password_reset(request):
    return render(request,'password_reset.html')
@login_required
def properties(request):
    projects=get_project_list()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    context={
        "project_list":projects,
        "Properties":"active",
        "last_url_word":last_url_word,
    }
    return render(request,'administrator/properties.html',context)
@login_required
def project_update(request, id):
    if request.method=="POST":
        project = get_object_or_404(Project, id=id)
        project.city=request.POST.get('city')
        project.name=request.POST.get('name')
        project.description=request.POST.get('description')
        project.view=request.POST.get('view')
        project.is_verified=request.POST.get('is_verified')
        project.is_for_rent=request.POST.get('is_for_rent')
        project.title=request.POST.get('title')
        project.sub_area=request.POST.get('sub_area')
        project.property_type=request.POST.get('property_type')
        project.category=request.POST.get('category')
        project.sub_category=request.POST.get('sub_category')
        project.website=request.POST.get('website')
        location_id=request.POST.get('location')
        try:
            location=Location.objects.get(id=location_id)
            project.location=location
        except:
            pass
        project.amenities=request.POST.get('amenities')
        project.nearby=request.POST.get('nearby')
        project.construction_status=request.POST.get('construction_status')
        project.status=request.POST.get('status')
        project.furnished=request.POST.get('furnished')
        project.security_deposit=request.POST.get('security_deposit')
        project.rent_property=request.POST.get('rent_property')
        project.rent_escalation_period=request.POST.get('rent_escalation_period')
        project.rent_priority_comment=request.POST.get('rent_priority_comment')
        project.size=request.POST.get('size')
        project.carpet_area=request.POST.get('carpet_area')
        project.type=request.POST.get('type')
        project.builder=request.POST.get('builder')
        project.floor=request.POST.get('floor')
        project.total_floor=request.POST.get('total_floor')
        project.facing=request.POST.get('facing')
        project.possession_type=request.POST.get('possession_type')
        project.is_rented=request.POST.get('is_rented')
        project.rent=request.POST.get('rent')
        project.cost=request.POST.get('cost')
        project.extra_charge=request.POST.get('extra_charge')
        project.lease_time=request.POST.get('lease_time')
        project.lease_completed=request.POST.get('lease_completed')
        project.lease_balance=request.POST.get('lease_balance')
        project.rent_escalation=request.POST.get('rent_escalation')
        project.rent_to=request.POST.get('rent_to')
        project.maintenance=request.POST.get('maintenance')
        project.registry=request.POST.get('registry')
        project.transfer_charge=request.POST.get('transfer_charge')
        project.gst=request.POST.get('gst')
        project.profit_sharing=request.POST.get('profit_sharing')
        project.roi=request.POST.get('roi')
        project.profile_pic=request.POST.get('profile_pic')
        project.shop_for=request.POST.get('shop_for')
        project.posted_by=request.POST.get('posted_by')
        project.possession_status=request.POST.get('possession_status')
        project.is_corner_plot=request.POST.get('is_corner_plot')
        project.hidden_notes=request.POST.get('hidden_notes')
        project.lock_in=request.POST.get('lock_in')
        project.power_breakup_rate=request.POST.get('power_breakup_rate')
        project.road_size=request.POST.get('road_size')
        publisher_name = request.POST.get('publisher')
        # Handle the publisher field
        publisher_id = request.POST.get('publisher')
        try:
            publisher=Publisher.objects.get(id=publisher_id)
            project.publisher=publisher
        except:
            pass
        project.meta_desc=request.POST.get('meta_desc')
        project.meta_key=request.POST.get('meta_key')
        project.is_distress=request.POST.get('is_distress')
        project.reason_distress=request.POST.get('reason_distress')
        project.cost_distress=request.POST.get('cost_distress')
        project.recommended=request.POST.get('recommended')
        project.plot_size=request.POST.get('plot_size')
        project.construction_age=request.POST.get('construction_age')
        project.code=request.POST.get('code')
        project.listing_date=request.POST.get('listing_date')
        project.slug=request.POST.get('slug')
        project.save()
        projectTab = get_object_or_404(projectTable, project=project)
        project=Project.objects.get(id=id)
        projectTab.project=project
        projectTab.price=request.POST.get('price')
        projectTab.locality=request.POST.get('locality')
        projectTab.topology=request.POST.get('topology')
        projectTab.neighbourhood=request.POST.get('neighbourhood')
        projectTab.master_plan=request.POST.get('master_plan')
        projectTab.unit_plan=request.POST.get('unit_plan')
        projectTab.save()
        from django.core.files.storage import FileSystemStorage
        picture = request.FILES.get('picture', None)
        image = request.FILES.get('image', None)
        image2 = request.FILES.get('image2', None)
        image3 = request.FILES.get('image3', None)
        image4 = request.FILES.get('image4', None)
         # Save files if they are uploaded
        fs = FileSystemStorage()
        if picture:
            picture_url = fs.save(picture.name, picture)
        if image:
            image_url = fs.save(image.name, image)
        if image2:
            image2_url = fs.save(image2.name, image2)
        if image3:
            image3_url = fs.save(image3.name, image3)
        if image4:
            image4_url = fs.save(image4.name, image4)
        return redirect('properties')
    location=Location.objects.all()
    project_list=get_project_list()
    project_df=pd.DataFrame(project_list)
    project_df=project_df[project_df["id"]==id]
    project_columns=project_df.columns
    project_data = project_df.to_dict(orient='records')
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    context={
        "project_data":project_data,
        'Properties':"active",
        "last_url_word":last_url_word,
        'project_columns':project_columns,
        'location':location,
    }
    return render(request,"administrator/project_update.html",context)

@login_required
def project_delete(request, id):
    if request.method == "POST":
        project = get_object_or_404(Project, id=id)
        try:
            project.delete()
            messages.success(request, 'Project deleted successfully.')
        except Exception as e:
            messages.error(request, f'Error deleting project: {e}')
        
        return redirect('properties')
    
    # Render a confirmation page if not a POST request
    project = get_object_or_404(Project, id=id)
    return render(request, 'administrator/project_confirm_delete.html', {'project': project})
from django.apps import apps


def get_all_models(app_name):
    try:
        app_config = apps.get_app_config(app_name)
        models = app_config.get_models()
        return [model for model in models]
    except LookupError:
        # print(f"App '{app_name}' not found.")
        return []


@login_required
def tables(request):
    app_name = 'myapp'
    models = get_all_models(app_name)
    models_list=[]
    for model in models:
        models_list.append((model.__name__))
    app_name = 'api'
    models = get_all_models(app_name)
    for model in models:
        models_list.append((model.__name__))

    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    context={
        "all_tables":models_list,
        'last_url_word':last_url_word,
    }
    return render(request,'administrator/all_tables.html',context)
@login_required
def views_table(request, name):
    model = None
    try:
        # Try to get the model from 'myapp'
        model = apps.get_model('myapp', name)
    except LookupError:
        try:
            # If not found, try to get the model from 'api'
            model = apps.get_model('api', name)
        except LookupError:
            # If the model is not found in both apps, return an error response
            return HttpResponse(f"No model found with name: {name}", status=404)
    
    # Fetch all objects from the model
    tables_data = model.objects.all().values()  # Convert QuerySet to a list of dicts

    # Convert to DataFrame
    table_df = pd.DataFrame(list(tables_data))
    
    # Handle empty DataFrame
    if table_df.empty:
        return HttpResponse(f"No data available for model: {name}", status=404)
    
    # Get columns names
    columns_name = table_df.columns.tolist()
    
    # Prepare data for template with zip
    zipped_data = [zip(columns_name, obj.values()) for obj in tables_data]
    
    # Get the last part of the URL
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    
    # Context for rendering
    context = {
        "zipped_data": zipped_data,
        'last_url_word': last_url_word,
        'columns_name': columns_name,
    }
    
    # Render the template with context
    return render(request, 'administrator/table_html.html', context)
@login_required
def add_project(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('properties')
    else:
        form = ProjectForm()
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]

    context = {
        "form": form,
        'Properties': "active",
        "last_url_word": last_url_word,
    }
    
    return render(request, 'administrator/add_project.html', context)   

@login_required
def add_table_data(request, name):
    form_class = buildForm(name)
    if request.method == 'POST':
        form = form_class(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()
            return redirect('tables')  # Replace with your success URL
    else:
        form = form_class()
    
    context = {
        "form": form,
    }
    return render(request, 'administrator/tablesForm.html', context)

def reffernow(request):
    return render(request,'ambessador/reffernow.html')

def project_details(request, id):
    # Get the project data
    project_data = get_project_list()
    
    # Create a DataFrame
    project_df = pd.DataFrame(project_data)
    
    # Filter the DataFrame for the given project id
    project_df = project_df[project_df['id'] == id]
    
    # Assuming there is only one row with the given id, convert that row to a dictionary
    project_details_dict = project_df.iloc[0].to_dict()
    
    # Get the full URL and extract the last word from it
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]

    # Prepare the context
    context = {
        "project_details": project_details_dict,
        'Properties': "active",
        "last_url_word": last_url_word,
    }
    
    # Render the template with the context
    return render(request, 'administrator/project_details.html', context)


def curated_events(request):
    return render(request,'ambessador/curated_events.html')

def life_trends(request):
    post_data = posts.objects.all()
    paginator = Paginator(post_data, 6)  # Show 6 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context={
        'page_obj': page_obj,
        }
    
    return render(request,'ambessador/life-trends.html',context)


def subscribe(request):
    response = HttpResponse("Subscription successful")
    response.set_cookie('subscribed', 'true', max_age=365*24*60*60)  # Cookie expires in one year
    return response
from pdfminer.high_level import extract_text_to_fp
from io import StringIO

def pdf_to_html(pdf_path):
    output_bytes = BytesIO()
    with open(pdf_path, 'rb') as fin:
        extract_text_to_fp(fin, output_bytes, output_type='html')
    return output_bytes.getvalue().decode('utf-8')

def posts_details(request, id):
    posts_data = get_object_or_404(posts, id=id)  # Adjust 'Posts' to match your model name
    # Define the destination directory
    destination_directory = 'myapp\static\pdf'

    # Copy the PDF file
    new_file_path = copy_pdf_to_other_location(posts_data, destination_directory)
    # Normalize the path (replace backslashes with forward slashes)
    file_path = new_file_path.replace("\\", "/")

    
    # Split the path by '/'
    parts = file_path.split('/')
    parts=parts[2:]
    seperator="/"
    pdf_url=seperator.join(parts)
    # pdf_url=parts.rstrip("/")
    

    all_posts_data = posts.objects.all()
    context = {
        'all_posts_data': all_posts_data,
        'posts_data': posts_data,
        'pdf_url':pdf_url,
    }

    return render(request, 'ambessador/posts_details.html', context)



def search(request):
    search_list = []
    project_list = get_project_list()  # This returns a list of dictionaries

    if request.method == "POST":
        # Get the form data
        property_type = request.POST.get('property_type')
        city = request.POST.get('city')
        status = request.POST.get('status')
        budget = request.POST.get('budget')

        # Filter the project list based on the search criteria
        for project in project_list:
            type_result = True if  project.get('property_type') == property_type else False
            city_result = True if   project.get('city') == city else False
            status_result = True if project.get('status') == status else False
            budget_result = True if  (project.get('price') and int(project.get('price')) >= int(budget)) else False
            if type_result or city_result or status_result or budget_result:
                # print("ALl True Data")
                search_list.append(project)

    # For demonstration purposes: Load country flags CSV
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)

    # Get the full URL and extract the last segment
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    # print(search_list)
    chatbot_data = request.session.get('chatbot_data', {})
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    

    context = {
        "project_list":project_list,  # Show filtered list or original list
        "country_flag_df": country_flag_df,
        'last_url_word': last_url_word,
        'search_list':search_list,
        'chatbot_data': chatbot_data,
        'city':city,
    }

    return render(request, 'search.html', context)



@csrf_exempt  # Exempt from CSRF verification for simplicity, but consider security implications
def chatbot_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            # Save data to the chatboatData model
            user_data = chatboatData.objects.create(
                name=data.get('name'),
                mobile=data.get('mobile'),
                email=data.get('email')
            )

            # Return success response with the created user's ID
            return JsonResponse({'status': 'success', 'id': user_data.id})

        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    

def getmap(request):
    # Example data, replace this with your actual data retrieval logic
    project_list = get_project_list()
    project_list = Project.objects.all()
    latitudes=[]
    longitudes=[]
	
    for project in project_list:
        # print(project["latitude"])
        # print(project["longitude"])
        latitudes.append(float(project["latitude"]))
        longitudes.append(float(project["longitude"]))

    # Initialize the gmplot object with a center point and zoom level
    # Here, we take the average latitude and longitude for the center
    center_lat = sum(latitudes) / len(latitudes)
    center_lng = sum(longitudes) / len(longitudes)
    gmap = gmplot.GoogleMapPlotter(center_lat, center_lng, 4)

    # Plot the points on the map
    gmap.scatter(
    latitudes, 
    longitudes, 
    color='red', 
    size=20, 
    marker=True, 
    edge_width=2.0, 
    face_alpha=0.8, 
    edge_alpha=1.0, 
    edge_color='black'
    )


    # Draw the map and save it to the static folder
    map_path ='static/map.html'
    gmap.draw(map_path)

    # Return the URL of the map
    return JsonResponse({'map_url': 'static/map.html'})

@csrf_exempt
def sitevisiter_insert(request):
    if request.method == 'POST':
        mobile = request.POST.get('mobile')
        name=request.POST.get('name')
        email=request.POST.get('email')
        try:
            visiter=sitevisiter.objects.get(mobile=mobile)
            visiter.email=email
            visiter.created_at=timezone.now()
            visiter.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        except:
            # Save data to the sitevisiter model
            user_data = sitevisiter(
               mobile = mobile,
               name = name,
               email = email
            )
            user_data.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
def update_record(request, model_name, pk):
    # Dynamically get the model class based on the model name
    form_class = buildForm(model_name)
    ModelClass=None
    try:
        ModelClass = apps.get_model(app_label='api', model_name=model_name)
    except:
        ModelClass = apps.get_model(app_label='myapp', model_name=model_name)
    instance = get_object_or_404(ModelClass, pk=pk)
    
    # Dynamically create a ModelForm for the model
    FormClass = modelform_factory(ModelClass, fields='__all__')

    if request.method == 'POST':
        form = FormClass(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('tables')
        else:
            return JsonResponse({'status': 'error', 'errors': form.errors})

    form = FormClass(instance=instance)
    context={
        'form': form,
        'instance': instance
        }
    return render(request, 'administrator/update_form.html', context)
@login_required
def delete_record(request, model_name, pk):
    ModelClass = None
    try:
        ModelClass = apps.get_model(app_label='api', model_name=model_name)
    except LookupError:
        ModelClass = apps.get_model(app_label='myapp', model_name=model_name)
    
    instance = get_object_or_404(ModelClass, pk=pk)

    # Check if the user has permission to delete this object
    if not request.user.has_perm('delete_{}'.format(model_name.lower()), instance):
        raise PermissionDenied
    
    instance.delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@csrf_exempt  # Exempt CSRF validation for demonstration (use with caution)
def search_history(request):
    if request.method == 'POST':
        try:
            # Extract data from the request body
            data = json.loads(request.body)
            csrftoken = data.get('csrftoken')
            filter_value = data.get('filter')

            if not csrftoken:
                return JsonResponse({'error': 'CSRFTOKEN is required'}, status=400)

            # Get the visiter based on the csrftoken
            try:
                visiter = sitevisiter.objects.get(csrftoken=csrftoken)
            except sitevisiter.DoesNotExist:
                return JsonResponse({'error': 'User not found'}, status=404)

            # Save the search history record
            search_record = searchHistory(
                user=visiter,
                searches=filter_value,
                url=request.build_absolute_uri(),
            )
            search_record.save()

            # Filter search history
            filtered_searches = searchHistory.objects.filter(
                user=visiter,
                searches__icontains=filter_value
            )

            # Prepare the response data
            data = list(filtered_searches.values('searches', 'url', 'created_at'))
            return JsonResponse(data, safe=False)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)



def getmapwidthproject(request, id):
    # Example data, replace this with your actual data retrieval logic
    project_list = get_project_list()
    latitudes = []
    longitudes = []

    for project in project_list:
        if int(project["id"]) == id:
            latitudes.append(float(project["latitude"]))
            longitudes.append(float(project["longitude"]))

    # Initialize the gmplot object with a center point and zoom level
    center_lat = sum(latitudes) / len(latitudes) if latitudes else 0
    center_lng = sum(longitudes) / len(longitudes) if longitudes else 0
    gmap = gmplot.GoogleMapPlotter(center_lat, center_lng, 9)

    # Plot the points on the map
    gmap.scatter(
        latitudes, 
        longitudes, 
        color='red', 
        size=20, 
        marker=True, 
        edge_width=2.0, 
        face_alpha=0.8, 
        edge_alpha=1.0, 
        edge_color='black'
    )

    # Draw the map and save it to the static folder
    map_path = 'static/map.html'
    gmap.draw(map_path)

    # Return the URL of the map
    map_url = 'static/map.html'
    return JsonResponse({'map_url': map_url})




@csrf_exempt
def save_url_in_history(request):
    if request.method == 'POST' and request.user.is_authenticated:
        url = request.build_absolute_uri()
        csrftoken=request.POST.get('csrftoken')
        visiter=get_object_or_404(sitevisiter,csrftoken=csrftoken)
        # visiter = getattr(request.user, 'sitevisiter', None)

        # Save the history entry
        History.objects.create(
            visiter=visiter,
            action=url.rstrip('/').split('/')[-1],
            url=url,
            record_id=0,  # Adjust if you want to capture a specific record ID
            description=f"Visited {url}",
            timestamp=timezone.now()
        )
        
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

def scheduletime(request):
    if request.method=="POST":
        firsName=request.POST.get("firstName")
        lastName=request.POST.get("lastName")
        email=request.POST.get('email')
        countryName=request.POST.get('countryName')
        mobile=request.POST.get('mobile')
        inputdate=request.POST.get('date')
        inputtime=request.POST.get('time')
        project=request.POST.get('project')
        ins=schedulOn(
            firstName =  firsName,
            lastName =  lastName,
            email =  email,
            country =  countryName,
            mobile =  mobile,
            schedule_data =  inputdate,
            schedule_time =  inputtime,
            projectName =  project
        )
        ins.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def membership(request):
    offer=membershipOffer.objects.all()
    
    # print(offer)
    context={
        'offers':offer,
    }
    return render(request,'ambessador/membership.html',context)
    
def ambessador_units(request):
    customer_id = request.session.get('customer_id')
    if request.method == "POST":
        project_id = request.POST.get('project')
        unit = request.POST.get('units_no')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        
        # Fetch the related objects
        customer_instance = get_object_or_404(customer, id=customer_id)
        project_instance = get_object_or_404(Project, id=project_id)
        
        # Create and save the CustomerLead instance
        customer_lead_instance = customerLead(
            customer=customer_instance,
            project=project_id,
            units=unit,
            email=email,
            mobile=mobile
        )
        customer_lead_instance.save()
        
        # Redirect after saving
        return redirect("ambessador/")
    customer_data=get_object_or_404(customer,id=customer_id)
    project=projectTable.objects.all()
    context={
        'units':True,
        'project':project,
        'customer_data':customer_data,
    }
    return render(request,'ambessador/customer.html',context)


def project_callus(request):
    if request.method=="POST":
        city=request.POST.get('city')
        project=request.POST.get('project')
        countryName=request.POST.get('countryName')
        countryCode=request.POST.get('countryCode')
        mobile=request.POST.get('mobile')
        ins=projectCallus(
            countryName=countryName,
            countryCode=countryCode,
            city=city,
            mobile=mobile,
            projectName=project
        )
        ins.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))

def contactus(request):
    # Read the CSV files
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    # print(city_df)
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_list = get_project_list()
    project_field_names = [field.name for field in Project._meta.get_fields() if not field.many_to_one]
    # Retrieve all Project records
    projects_data = Project.objects.all().values(*project_field_names)
    zipped_projects = []
    for project in projects_data:
        zipped_project = dict(zip(project_field_names, [project[field] for field in project_field_names]))
        zipped_projects.append(zipped_project)
    projects_df=pd.DataFrame(list(project_list))
    city=projects_df['city'].unique()
    context = {
        "project_list": project_list,
        "country_flag_df": country_flag_df,
        'last_url_word': last_url_word,
        'zipped_projects':zipped_projects,
        'city':city,
    }
    return render(request, "contact.html", context)
def projectMapView(request):
    projects = Project.objects.all()
    project_list2 = []
    for project in projects:
        project_list2.append({
            "id":project.id,
            "title": project.title,
            "location": project.location.city,
            "latitude": project.location.latitude,
            "longitude": project.location.longitude
        })
        # Load the country flag data
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    
    # Get the current URL and extract the last part
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    project_list=get_project_list()
    projects_df=pd.DataFrame(project_list)
    city=projects_df['city'].unique()
    # Prepare context for the template
    context = {
        "project_list":project_list,
        "project_list2": project_list2,
        "country_flag_df": country_flag_df.to_dict(orient='records'),  # Convert DataFrame to a list of dicts
        "last_url_word": last_url_word,
        "city":city,
    }
    return render(request, "map.html", context)

def city_project(request,city):
    # Load the country flag data
    country_flag_df = pd.read_csv('myapp/static/Countyr_list_code_flag.csv', index_col=False)
    
    # Get the current URL and extract the last part
    full_url = request.build_absolute_uri()
    last_url_word = full_url.rstrip('/').split('/')[-1]
    city_project_list = Project.objects.filter(location__city=city)
    print(city_project_list)
    print(city_project_list)
    project_list=get_project_list()
    projects_df=pd.DataFrame(project_list)
    city=projects_df['city'].unique()
    print(city_project_list)
    context = {
        "project_list":project_list,
        "city_project_list": city_project_list,
        "country_flag_df": country_flag_df.to_dict(orient='records'),  # Convert DataFrame to a list of dicts
        "last_url_word": last_url_word,
        "city":city,
    }
    return render(request,'city_project.html',context)

def log_project_click(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        href = data.get('href')
        csrf = data.get('id')
        discription=data.get('discription')

        History.objects.create(
            visiter=request.user.sitevisiter if request.user.is_authenticated else None,
            action="Click",
            url=href,
            record_id=csrf,
            description=f"User clicked on {discription}",
            timestamp=timezone.now()
        )
        return JsonResponse({'status': 'success'})
    
    
    
        




