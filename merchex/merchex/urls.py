"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name="band-list"),
    path('bands/<int:band_id>/', views.band_detail, name="band-detail"), # with name you can refer to this path in the templates {% url 'name' %}
    path('about-us/', views.about, name="about"),
    path('contact-us/', views.contact, name="contact"),
    path('listings/', views.list, name="list-list"),
    path('listings/<int:list_id>/', views.list_detail, name="list-detail"), # <int:list_id> to pass the id to the function in views.list_detail(request, list_id)
    path('email-confirmation/', views.email_sent, name="email-sent")
]
