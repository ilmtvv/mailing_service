from django.urls import path


from output_messages.apps import OutputMessagesConfig
from output_messages.views import MessagesListView, MessageCreateView, MessageUpdateView, DeleteMessageView

app_name = OutputMessagesConfig.name

urlpatterns = [
    path('', MessagesListView.as_view(), name='messages_list'),
    path('create/', MessageCreateView.as_view(), name='message_create'),
    path('update/<int:pk>/', MessageUpdateView.as_view(), name='message_update'),
    path('delete/<int:pk>/', DeleteMessageView.as_view(), name='delete_message'),

]