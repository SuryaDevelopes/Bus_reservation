from django.urls import re_path
from django.contrib.auth import views as auth_views
from . import views
app_name = 'account'
urlpatterns = [
    re_path(r'^register/$',views.register,name='register'),
    re_path(r'^my_account/$',views.my_account,name= 'my_account'),
    re_path(r'^ticket-details/(?P<ticket_id>[−\w]+)/$', views.ticket_details,name='ticket_details'),
    re_path(r'^accounts/login/$', auth_views.LoginView.as_view() ,{'template_name': 'registration/login.html' }, name='login'),
]
