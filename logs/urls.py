from django.urls import path

from logs.apps import LogsConfig
from logs.views import LogListView

app_name = LogsConfig.name

urlpatterns = [
    path('', LogListView.as_view(), name='log_list'),

]