"""nazox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls.conf import include
from nazox import views
from django.urls import include
from django.contrib.auth.decorators import login_required
from nazox.views import MyPasswordChangeView,MyPasswordSetView


urlpatterns = [
    # Menu    
    path('',views.DashboardView.as_view(),name='dashboard'),# Dashboard
    path('menu/calendar',views.CalendarView.as_view(),name='calendar'),# Calender
    path('menu/chat',views.ChatView.as_view(),name='chat'),# Chat
    path('menu/app-kanban-board',views.KanbanBoardView.as_view(),name='app-kanban-board'),# Kanban Board
    path('menu/settings',views.SettingsView.as_view(),name='settings'),# Settings
   
    # Apps 
    path('ecommerce/',include('ecommerce.urls')),# Ecommerce
    path('email/',include('mail.urls')),# Email
    path('layouts/',include('layouts.urls')),# Layout
    path('pages/',include('utility.urls')),# Utility
    path('components/',include('components.urls')),# Components
    path('admin/', admin.site.urls),# Admin
    
    path(
        "accounts/password/change/",
        login_required(MyPasswordChangeView.as_view()),
        name="account_change_password",
    ),
    path(
        "accounts/password/set/",
        login_required(MyPasswordSetView.as_view()),
        name="account_set_password",
    ),
    
    
    # Include the allauth and 2FA urls from their respective packages.
    path('account/', include('allauth_2fa.urls')),
    path('account/', include('allauth.urls')),
]
