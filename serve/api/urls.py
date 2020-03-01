from django.urls import path

from .views import MovieAPIView

urlpatterns = [
    path('', MovieAPIView.as_view()),
]