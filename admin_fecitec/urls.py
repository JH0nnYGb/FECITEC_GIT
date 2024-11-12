from django.urls import path, include
from admin_fecitec.views import index

app_name = 'admin_fecitec'

urlpatterns = [
    path('index/',index, name='index'),

]