from django.urls import path

from .views import MovieAPIView
from .views import MovieAPIViewIDBase

urlpatterns = [
    path('', MovieAPIView.as_view()),
    path('<int:pk>/', MovieAPIViewIDBase.as_view())
]