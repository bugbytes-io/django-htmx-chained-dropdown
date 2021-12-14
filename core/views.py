from django.shortcuts import render
from core.models import Course, Module

# Create your views here.
def courses(request):
    courses = Course.objects.all()
    context = {'courses': courses}
    return render(request, 'university.html', context)


def modules(request):
    course = request.GET.get('course')
    modules = Module.objects.filter(course=course)
    context = {'modules': modules}
    return render(request, 'partials/modules.html', context)
