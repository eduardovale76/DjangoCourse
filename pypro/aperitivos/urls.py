from django.urls import path, include

from pypro.aperitivos.views import video
app_name='aperitivos'
urlpatterns = [
    path('<slug:slug>', video, name='video'),

]