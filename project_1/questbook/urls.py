from django.urls import path
from .views import index
urlpatterns = [
    path('questbook', index, name="index")
    
]