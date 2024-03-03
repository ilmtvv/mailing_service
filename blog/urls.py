from django.urls import path

from blog.apps import BlogConfig
from blog.views import BlogUnitDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('<int:pk>/', BlogUnitDetailView.as_view(), name='detail_unit'),

]
