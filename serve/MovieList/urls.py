
from django.urls import path, include
from serve import views

urlpatterns = [
    path('', include('serve.urls')),
    path('movie/', include('api.urls'))
]
