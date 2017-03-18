"""ChexBox URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls.defaults import *
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^', include('box.urls')),
    url(r'^admin/', admin.site.urls),
    
    url(r'^accounts/login/$', auth_views.login, name='login'),
    url(r'^accounts/logout/$', auth_views.logout, name='logout'),       
    url(r'^accounts/password/reset/$', 
        auth_views.password_reset, 
        {'post_reset_redirect' : 'password_reset_done'},
        name='password_reset'),
    url(r'^accounts/password/reset/done/$',
        auth_views.password_reset_done, name='password_reset_done'),
    url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,  
        {'post_reset_redirect' : 'password_reset_complete'}, name='password_reset_confirm'),
    url(r'^accounts/password/done/$', 
        auth_views.password_reset_complete, name='password_reset_complete'),
               
#     url(r'^$', login_views.index, name='index'),
#     url(r'^home/$', login_views.FileListView.as_view(), name='home'),            
#     url(r'^add$',  login_views.upload_file, name='chexbox-add'),
#     url(r'^accounts/register/$', login_views.register, name='register'),
#     url(r'^accounts/register/complete/$', login_views.registration_complete, 
#       name='registration_complete'),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

