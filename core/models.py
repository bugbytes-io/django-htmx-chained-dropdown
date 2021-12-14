from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=128)


class Module(models.Model):
    name = models.CharField(max_length=128)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')