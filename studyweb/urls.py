"""studyweb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from myweb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('vmsinfo/', views.get_cvms_info),
    path('add/', views.add_event),
    path('about/', views.about),
    path('insertdata/', views.insertdata),
    path('hg/', views.get_hight_info),
    path('dealevent/', views.insert_deal_event),
    path('vmchange/', views.insert_vmchange),
    path('getfile/', views.get_files),
    path('table/', views.table_fy),
    path('searchip/', views.search_ip),
]
