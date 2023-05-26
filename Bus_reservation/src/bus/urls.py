from django.urls import re_path
from . import views
app_name = 'bus'
urlpatterns  = [
    re_path(r'^$',views.index,name='index'),
#     url (r'^category/(?P<category_slug>[−\w]+)/$',views.show_category, name='catalog_category'),
    re_path(r'^search-bus/$', views.search_bus,name='searchBus'),
    re_path(r'^autocomplete_pick/$', views.autocomplete_pick,name='pickareas'),
    re_path(r'^autocomplete_drop/$', views.autocomplete_drop,name='dropareas'),
]
