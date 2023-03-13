from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include("django.contrib.auth.urls")),
    path('oauth/', include("social_django.urls")),
    path('', include('user_profile.urls')),
]
