from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('edit_photo/<int:pk>', views.edit_photo, name='edit_photo'),
    path('edit_about/<int:pk>', views.edit_about, name='edit_about'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('photo/<int:pk>', views.photo, name='photo'),
    path('delete_photo/<int:pk>', views.delete_photo, name='delete_photo'),
    path('settings/<int:pk>', views.settings, name='settings'),
    path('search/', views.search, name='search')
]
