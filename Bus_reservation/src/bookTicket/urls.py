from django.urls import re_path
from . import views
app_name = 'bookTicket'
urlpatterns  = [
    re_path(r'^book-ticket/(?P<bus_id>[−\w]+)/$', views.book_ticket,name='bookTicket'),
]
