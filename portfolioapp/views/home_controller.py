from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, "Home.html")

def cv(request):
    
    return render(request, "CV.html")