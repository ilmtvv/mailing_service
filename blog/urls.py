from django.urls import path
from django.views.decorators.cache import cache_page

from blog.apps import BlogConfig
from blog.views import BlogUnitDetailView

app_name = BlogConfig.name

urlpatterns = [
    path('<int:pk>/', cache_page(333)(BlogUnitDetailView.as_view()), name='detail_unit'),

]
