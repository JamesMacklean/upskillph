from unicodedata import name
from django.contrib import admin
from django.urls import path,include, re_path
from . import views
from .views import SessionChecker

# All registered urls
urlpatterns = [
    path('',views.home, name="home"),
    path('account/', views.account, name="account"),
    path('administrator/', views.admin_dashboard, name='admin_dashboard'),
    path('administrator/users/', views.user_management, name='user_management'),
    path('administrator/users/<int:user_id>/', views.user_details, name='user_details'),
    path('administrator/partner/<int:partner_id>/', views.admin_partners, name='admin_partners'),
    path('administrator/license-codes/<slug>/', views.license_codes, name='license_codes'),
    path('certificate/', views.certificate, name="certificate"),
    path('dashboard/', views.applied_programs, name="dashboard"),
    path('partner/', views.partner, name="partner"),
    path('partner/<slug:program_slug>/application/', views.application, name="application"),
    path('profile/', views.profile, name="profile"),
    path('profile/edit/', views.edit_profile, name="edit"),
    path('program/<slug>/', views.program, name="program"),
    path('sessions/', SessionChecker.as_view(), name="sessions"),
    path('signin/',views.signin, name="signin"),
    path('signout/',views.signout, name="signout"),
    path('signup/',views.signup, name="signup"),
    path('success/<user_hash>/', views.success, name="success"),
    path('verify/<user_hash>/', views.verify_account, name="verify_account"),

    path('guidelines/',views.guidelines, name="guidelines"),
    path('privacy/', views.privacy, name="privacy"),
    path('contact-us/', views.contact, name="contact"),
    path('lakip/',views.lakip_landing, name='lakip-landing'),
    path('lakip/apply/',views.lakip_application, name='lakip-application'),
    
    # COURSERA
    # path('refresh/', views.refresh_token, name="refresh"),
]

# URLs for 'accounts' subdomain
accounts_urlpatterns = [
    path('signin/', views.signin, name="signin"),
    path('signout/', views.signout, name="signout"),
    path('signup/', views.signup, name="signup"),
    path('success/<user_hash>/', views.success, name="success"),
    path('verify/<user_hash>/', views.verify_account, name="verify_account"),
]

# URLs for 'welcome' subdomain
welcome_urlpatterns = [
    path('', views.home, name="home"),
    path('account/', views.account, name="account"),
    path('administrator/', views.admin_dashboard, name='admin_dashboard'),
    path('administrator/users/', views.user_management, name='user_management'),
    path('administrator/users/<int:user_id>/', views.user_details, name='user_details'),
    path('administrator/partner/<int:partner_id>/', views.admin_partners, name='admin_partners'),
    path('administrator/license-codes/<slug>/', views.license_codes, name='license_codes'),
    path('certificate/', views.certificate, name="certificate"),
    path('dashboard/', views.applied_programs, name="dashboard"),
    path('partner/', views.partner, name="partner"),
    path('partner/<slug:program_slug>/application/', views.application, name="application"),
    # path('partner/<slug:program_slug>/profile/', views.partner_profile, name="partner_profile"),
    path('profile/', views.profile, name="profile"),
    path('profile/edit/', views.edit_profile, name="edit"),
    path('program/<slug>/', views.program, name="program"),
    path('sessions/', SessionChecker.as_view(), name="sessions"),
    path('guidelines/', views.guidelines, name="guidelines"),
    path('privacy/', views.privacy, name="privacy"),
    path('contact-us/', views.contact, name="contact"),
    path('lakip/', views.lakip_landing, name='lakip-landing'),
    path('lakip/apply/', views.lakip_application, name='lakip-application'),
    
]