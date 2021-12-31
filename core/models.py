from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Module(models.Model):
    name = models.CharField(max_length=128)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')

    def __str__(self):
        return self.name