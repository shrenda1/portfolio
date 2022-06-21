from django import views
from django.urls import URLPattern, path
from portfolioapp.views import home_controller, cv_controller
urlpatterns = [
    path('', home_controller.home, name="home"),
    path('cv', cv_controller.cv, name = "cv"),
]