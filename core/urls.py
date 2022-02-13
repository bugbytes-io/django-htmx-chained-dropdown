from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('modules/', views.modules, name='modules'),
    path('info/', views.index, name='index'),
    path('courselist/', views.course_list, name='course-list')

]