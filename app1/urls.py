from django.urls import path
from . import views


urlpatterns = [
    path('',views.homefn,name='home'),
    path('detailsurl',views.detailfn,name='detailsurl'),


]
