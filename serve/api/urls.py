from django.urls import path

from .views import MovieAPIView
from .views import MovieAPIViewIDBase
from .views import MovieAPIViewNameBase
from .views import MovieAPIViewYearBase
from .views import MovieAPIViewYearNoBase

urlpatterns = [
    path('', MovieAPIView.as_view()),
    path('<int:pk>/', MovieAPIViewIDBase.as_view()),
    path('name/', MovieAPIViewNameBase.as_view()),
    path('year/', MovieAPIViewYearBase.as_view()),
    path('year/<int>/', MovieAPIViewYearNoBase.as_view()),
]