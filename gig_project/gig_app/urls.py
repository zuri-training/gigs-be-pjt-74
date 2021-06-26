from django.urls import path
from .views import Register, Success

urlpatterns = [
    path('', Success, name= 'success'),
    path('register/', Register.as_view(), name='register'),
]
