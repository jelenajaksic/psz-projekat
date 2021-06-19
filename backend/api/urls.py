from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'

urlpatterns = [
    path('realestate', views.get_all, name='get_all')
]

urlpatterns = format_suffix_patterns(urlpatterns)