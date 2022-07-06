from unicodedata import name
from django import views
from django.urls import URLPattern, path
from portfolioapp.views import home_controller, cv_controller, admin_controller
urlpatterns = [
    path('', home_controller.home, name="home"),
    path('admin/', admin_controller.adminlogin, name="adminlogin"),
    path('admin/dashboard', admin_controller.dashboard, name="dashboard"),
    path('delete_skill/<skill_id>', admin_controller.deleteskill, name="deleteskill"),
    path('skilladd', admin_controller.skilladd, name='skilladd'),
    path('delete_education/<education_id>', admin_controller.deleteeducation, name="delete_education"),
    path('educationadd', admin_controller.educationadd, name='educationadd'),
    path('personalinfoedit', admin_controller.personalinfoedit, name="personalinfoedit"),
    path('delete_project/<project_id>', admin_controller.projectdelete, name="projectdelete"),
    path('edit_project/<project_id>', admin_controller.projectedit, name="projectedit"),
    path('projecteditdata/<project_id>', admin_controller.projecteditdata, name="projecteditdata"),
    path('projectadd', admin_controller.projectadd, name='projectadd'),
    path('login', admin_controller.login, name="login"),
    path('logout', admin_controller.logout, name="logout"),
]