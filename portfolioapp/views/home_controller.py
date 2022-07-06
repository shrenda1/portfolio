from django.shortcuts import render
from portfolioapp.models.personal_information import personal
from portfolioapp.models.skills import skills
from portfolioapp.models.education import education
from portfolioapp.models.projects import projects
# Create your views here.
def home(request):
    personal_info = personal.objects.get(pk = 1)
    skill_data = skills.objects.all()
    education_data = education.objects.all()
    project_data = projects.objects.all()
    return render(request, "Home.html", {'personal_info':personal_info, 'skill_data': skill_data, 'education_data' : education_data, 'project_data' : project_data})