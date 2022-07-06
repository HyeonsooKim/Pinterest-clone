
from django.urls import path, include

from accountapp.views import hello_world

app_name = 'account_app'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world')
]