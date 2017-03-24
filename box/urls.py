from django.conf.urls import url

from . import views


#this app_name is important b/c Django needs to look through all the apps 
# and we need to differentiate
app_name = 'box'  
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.FileListView.as_view(), name='home'),
    url(r'^home/(?P<pk>[\w\-\ ]+)/delete/$', views.delete_file, name='delete_file'),
    url(r'^home/(?P<pk>[\w\-\ ]+)/favorite/$', views.favorite_file, name='favorite_file'),
    url(r'^add$',  views.upload_file, name='chexbox-add'),
    url(r'^accounts/register/$', views.register, name='register'),
    url(r'^accounts/register/complete/$', views.registration_complete, 
      name='registration_complete'),
    
    
]