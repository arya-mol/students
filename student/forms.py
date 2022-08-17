from student.models import *
from django.forms import ModelForm

class StudentForm(ModelForm):
    class Meta:
        model=Student
        fields="__all__"