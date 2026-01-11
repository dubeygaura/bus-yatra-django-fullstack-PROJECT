"""
URL configuration for bus_yatra project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('index_code/',views.index_code,name='index_code'),
    path('managebus/',views.managebus,name='managebus'),
    path('manage_routes/',views.manage_routes,name='manage_routes'),
    path('manage_quotas/',views.manage_quotas,name='manage_quotas'),
    path('bookin_view/',views.bookin_view,name='bookin_view'),
    path('manage_routes_code/',views.manage_routes_code,name='manage_routes_code'),
    path('manage_routes_delete/<int:id>',views.manage_routes_delete,name='manage_routes_delete'),
    path('managebus_code/',views.managebus_code,name='managebus_code'),
]
