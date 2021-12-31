from django.http import HttpResponse
from django.shortcuts import render
from .models import Course, Module
from .forms import UniversityForm

# Create your views here.
def courses(request):
    form = UniversityForm()
    context = {'form': form}
    return render(request, 'university.html', context)

def modules(request):
    form = UniversityForm(request.GET)
    # print(form['modules'])  # form['modules'] gives us HTML for <select>
    return HttpResponse(form['modules'])