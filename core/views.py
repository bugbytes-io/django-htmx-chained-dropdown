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


def index(request):
    context = {}
    return render(request, 'index.html', context)    

def course_list(request):
    courses = Course.objects.prefetch_related('modules').all()
    context = {'courses': courses}
    return render(request, 'partials/course-list.html', context)