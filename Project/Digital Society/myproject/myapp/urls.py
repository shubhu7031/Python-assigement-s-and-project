"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/',views.logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('changepassword/',views.changepassword,name='change_password'),
    path('editprofile/',views.editprofile,name='edit_profile'),
    path('notfound/',views.notfound,name='notfound'),
    path('addnotice/',views.add_notice,name='add_notice'),
    path('view-notice/',views.viewnotice,name='view_notice'),
    path('add-member/',views.add_member,name='add_member'),
    path('demo/',views.demo,name='demo'),
    path('all-notice/',views.all_notice,name='all_notice'),
    path('all-member/',views.all_member,name='all_member'),
    path('update-otp/',views.update_OTP,name='update_OTP'),
    path('Member-profile',views.profileM,name="member-profile"), 
    path('Member-notice', views.view_notice_M, name='member-notice'),
    path('changepasswordM/',views.update_password_M,name='update_password_M'),

]
