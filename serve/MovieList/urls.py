
from django.urls import path
from serve import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
]
