from django.urls import path
from .views.home import HomeView
from .views.profile import ProfileDelete, ProfileCreate, ProfileUpdate

app_name = 'user_profile'

urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('profile/create/', ProfileCreate.as_view(), name='profile_create'),
    path('profile/update/<int:pk>/', ProfileUpdate.as_view(), name='profile_update'),
    path('profile/delete/<int:pk>/', ProfileDelete.as_view(), name='profile_delete'),
]
