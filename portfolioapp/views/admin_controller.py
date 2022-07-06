from cgitb import reset
from email import message
from pydoc import describe
from turtle import tilt
from unicodedata import name
from django.shortcuts import redirect, render
from portfolioapp.models.personal_information import personal
from portfolioapp.models.skills import skills
from portfolioapp.models.education import education
from portfolioapp.models.projects import projects
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def adminlogin(request):
    if request.GET.get('next', None):
        messages.info(request, 'Plesae Login First')
    return render(request, "admin/loginpage.html")

@login_required(login_url="/admin/")
def dashboard(request):
    user = request.user
    personal_info = personal.objects.get(pk = 1)
    skill_data = skills.objects.all()
    project_data = projects.objects.all()
    education_data = education.objects.all()

    return render(request, "admin/dashboard_main.html", {'personal_info':personal_info, 'skill_data': skill_data, 'education_data' : education_data, 'project_data': project_data, 'userdata': user})

def deleteskill(request, skill_id):
    skill_d = skills.objects.get(pk=skill_id)
    skill_d.delete()
    return redirect('dashboard')

def skilladd(request):
    if request.method == "POST":
        skill_name = request.POST['skill_name']
        skill_insert = skills(skill_name = skill_name)
        skill_insert.save()
    return redirect('dashboard')

def deleteeducation(request, education_id):
    education_d = education.objects.get(pk=education_id)
    education_d.delete()
    return redirect('dashboard')

def educationadd(request):
    if request.method == "POST":
        education_level = request.POST['educationlevel']
        school_name = request.POST['schoolname']
        end_year = request.POST['endyear']
        education_d = education(education_level = education_level, school_name = school_name, end_year = end_year)
        education_d.save()
    return redirect('dashboard')

def personalinfoedit(request):
    if request.method == "POST":
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        email = request.POST['email']
        address = request.POST['address']
        contact = request.POST['contact']
        description = request.POST['description']
        personal_info = personal.objects.get(pk = 1)
        personal_info.first_name = first_name
        personal_info.last_name = last_name
        personal_info.email = email
        personal_info.address = address
        personal_info.contact = contact
        personal_info.description = description
        personal_info.save()
    return redirect('dashboard')

def projectadd(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        link = request.POST['link']
        project_d = projects(title = title, description = description, link = link)
        project_d.save()
    return redirect('dashboard')

def projectdelete(request, project_id):
    project_d = projects.objects.get(pk = project_id)
    project_d.delete()
    return redirect('dashboard')

def projectedit(request, project_id):
    project_d = projects.objects.get(pk = project_id)
    return render(request, 'admin/dashboard_main.html', {'projectdata':project_d})

def projecteditdata(request, project_id):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        link = request.POST['link']
        project_d = projects.objects.get(pk = project_id)
        project_d.title = title
        project_d.decsription = description
        project_d.link = link
        project_d.save()
    return redirect('dashboard')
    

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user= auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            print('Invalid')
            return redirect('login')
    else:
        return render(request, "admin/loginpage.html")

def logout(request):
    auth.logout(request);
    return redirect('admin/')


    