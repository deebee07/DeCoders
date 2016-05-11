"""AttendanceDisplay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls.static import static
from AttendanceDisplay import settings
from rest_framework.urlpatterns import format_suffix_patterns
from displayAttend import Get_REST
from django.conf.urls import include
from displayAttend import Post_REST


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$','displayAttend.views.home',name='home'),
    url(r'^attendance/$', 'displayAttend.views.attend', name='attend'),
    url(r'^studentattendance/$', 'displayAttend.views.studentAttend', name='studentattend'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    url(r'^api/getclasstoken/(?P<class_id>[0-9]+)/$',Get_REST.processTokenRequests ,name='RaspToken'),
    url(r'^api/getclasscodes/$',Get_REST.getClassCodes ,name='getClassCodes'),

    url(r'^api/postattendance/$',Post_REST.markAttendance ,name='markAttendance'),
    url(r'^api/registerstudent/$',Post_REST.registerStudent ,name='registerStudent'),
    url(r'^api/checkoutstudent/$',Post_REST.checkoutStudent ,name='checkoutStudent'),  



]
