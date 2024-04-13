from django.urls import path
from . import views

urlpatterns = [
    path('chats/<int:pk>', views.chats, name='chats'),
    path('chat/<int:pk>', views.chat, name='chat'),
    path('delete_message/<int:id>', views.delete_message, name='delete_message')
]