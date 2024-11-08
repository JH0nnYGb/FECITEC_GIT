from django.urls import path, include
from . import views

app_name = 'admin_fecitec'

urlpatterns = [
    path('', include('fecitec.urls')),
    path('index/',views.index, name='index'),

]