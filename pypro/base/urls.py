from django.urls import path, include

from pypro.base.views import home

app_name='base'
urlpatterns = [
    path('', home, name='home'),

]