from django import views
from django.urls import URLPattern, path
from portfolioapp import views
urlpatterns = [
    path('', views.home, name="home"),
    path('cv', views.cv, name = "cv"),
]