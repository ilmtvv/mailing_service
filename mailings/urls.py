from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import MailingListView, MailingCreateView, MailingUpdateView, DeleteMailingView

app_name = MailingsConfig.name

urlpatterns = [
    path('', MailingListView.as_view(), name='mailing_list'),
    path('create/', MailingCreateView.as_view(), name='mailing_create'),
    path('update/<int:pk>/', MailingUpdateView.as_view(), name='mailing_update'),
    path('delete/<int:pk>/', DeleteMailingView.as_view(), name='delete_mailing'),

]