from django.urls import path
from .views import ArtAPIView, ArtDetails
urlpatterns = [
    path('Art/', ArtAPIView.as_view()),
    path('Art/<int:id>/', ArtDetails.as_view()),
]