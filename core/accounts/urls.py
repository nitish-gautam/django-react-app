from django.urls import path
from accounts import views

urlpatterns = [
    # Leave as empty string for base url
    path('', views.index, name="index"),
]
