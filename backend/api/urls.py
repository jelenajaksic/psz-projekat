from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'

urlpatterns = [
    path('realestate', views.get_all, name='get_all'),
    path('most_common', views.get_most_common, name='get_most_common'),
    path('count_props_by_size', views.get_props_by_size, name='get_props_by_size'),
    path('count_props_by_year', views.get_props_by_year, name='get_props_by_year'),
    path('num_of_properties', views.get_number_of_properties,
         name='get_number_of_properties'),
    path('num_of_sell_by_city', views.get_number_of_properties_by_city,
         name='get_number_of_properties_by_city'),
    path('registration_count', views.get_registration,
         name='get_registration'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
