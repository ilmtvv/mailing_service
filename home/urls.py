from django.urls import path
from home.apps import HomeConfig
from home.views import home_view

app_name = HomeConfig.name

urlpatterns = [
    path('', home_view, name='home_view'),

]