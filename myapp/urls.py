
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myapp import views
from django.urls import path, include
from django.conf.urls import handler403, handler404

handler403 = 'myapp.views.custom_403_view'
handler404 = 'myapp.views.custom_404_view'



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.index,name="index"),
    path("project",views.project,name="project"),
    path("hometally",views.hometally,name="hometally"),
    path("aboutus",views.aboutus,name="aboutus"),
    path("management",views.management,name="management"),
    path("sustatnability",views.sustatnability,name="sustatnability"),
    path("design",views.design,name="design"),
    path("residential",views.residential,name="residential"),
    path("commercial",views.commercial,name="commercial"),
    path("finance",views.finance,name="finance"),
    path("investorInform",views.investorInform,name="investorInform"),
    path("governanceLeasership",views.governanceLeasership,name="governanceLeasership"),
    path("compliance",views.compliances,name="compliance"),
    path("csr",views.csr,name="csr"),
    path("discloser",views.discloser,name="discloser"),
    path("ballot",views.ballot,name="ballot"),
    path("dividend",views.dividend,name="dividend"),
    path("esop",views.esop,name="esop"),
    path("qip",views.qip,name="qip"),
    path("scheme",views.scheme,name="scheme"),
    path("credit",views.credit,name="credit"),
    path("procedure",views.procedure,name="procedure"),
    path("egm",views.egm,name="egm"),
    path("annual",views.annual,name="annual"),
    path("commission",views.commission,name="commission"),
    path("news",views.news,name="news"),
    path("pressreleas",views.pressreleas,name="pressreleas"),
    path("mediagallery",views.mediagallery,name="mediagallery"),
    path("legalinformation",views.legalinformation,name="legalinformation"),
    path("loanfornri",views.loanfornri,name="loanfornri"),
    path("nrifaq",views.nrifaq,name="nrifaq"),
    path("internationaloffice",views.internationaloffice,name="internationaloffice"),
    path("enqurenow",views.enqurenow,name="enqurenow"),
    path("blogs",views.blogs,name="blogs"),
    path("ambessador",views.ambessador,name="ambessador"), 
    path("project_enquiry",views.project_enquiry,name="project_enquiry"), 
    path("projectview/<int:id>",views.projectview,name="projectview"), 
    path("callback/<str:last_url_word>",views.callback,name="callback"), 
    path("real-estate-terms/<str:msg>",views.real_estate_terms,name="real-estate-terms"), 
    path("reachus",views.reachus,name="reachus"), 
    path("sendEmail",views.sendEmail,name="sendEmail"), 
    path("sendMobile",views.sendMobile,name="sendMobile"), 
    path("veryfyotp",views.verifyotp,name="veryfyotp"), 
    path("ambessador/customer/",views.ambessador_customer,name="ambessador/customer"), 
    path('administrator/login/', views.administratorlogin, name='administrator_login'),
    path('administrator/', views.administrator, name='administrator'),
    path('administrator/dashboard/', views.administrator_dashboard, name='administrator_dashboard'),
    path("administrator/password_reset/",views.password_reset,name="password_reset"), 
    path("administrator/properties",views.properties,name="properties"), 
    path("administrator/project_update/<int:id>/", views.project_update, name="project_update"),
    path("administrator/project_delete/<int:id>/", views.project_delete, name="project_delete"),
    path("administrator/tables", views.tables, name="tables"),
    path("administrator/views_table/<str:name>", views.views_table, name="views_table"),
    path("administrator/add_table_data/<str:name>", views.add_table_data, name="add_table_data"),
    path("administrator/add_project", views.add_project, name="add_project"),
    path("reffernow", views.reffernow, name="reffernow"),
    path("administrator/project_details/<int:id>/", views.project_details, name="project_details"),
    path("curated_events", views.curated_events, name="curated_events"),
    path("life-trends", views.life_trends, name="life-trends"),
    path("posts_details/<int:id>/", views.posts_details, name="posts_details"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
