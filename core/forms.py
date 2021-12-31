from django import forms
from dynamic_forms import DynamicField, DynamicFormMixin
from .models import Course, Module


class UniversityForm(DynamicFormMixin, forms.Form):

    def module_choices(form):
        course = form['course'].value()
        return Module.objects.filter(course=course)

    def initial_module(form):
        course = form['course'].value()
        return Module.objects.filter(course=course).first()        


    course = forms.ModelChoiceField(
        queryset=Course.objects.all(),
        initial=Course.objects.first()
    )
    modules = DynamicField(
        forms.ModelChoiceField,
        queryset=module_choices,
        initial=initial_module
    )
