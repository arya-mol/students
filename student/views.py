from django.shortcuts import render,redirect
from django.views.generic import View
from student.forms import StudentForm
from student.models import Student
# Create your views here.


class StudentList(View):
    def get(self,request,*args,**kwargs):
        students=Student.objects.all()
        context={"students":students}
        return render(request,"student_list.html",context)




class AddStudent(View):
    def get(self,request,*args,**kwargs):
        form=StudentForm()
        context={"form":form}
        return render(request,"add_student.html",context)
    def post(self,request,*args,**kwargs):
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("liststudent")

class StudentDetail(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        student=Student.objects.get(id=id)
        context={"student":student}
        return render(request,"student_detail.html",context)


class ChangeStudent(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        student=Student.objects.get(id=id)
        form=StudentForm(instance=student)
        context={"form":form}
        return render(request,"change_student.html",context)
    def post(self,request,*args,**kwargs):
        id=kwargs["id"]
        student=Student.objects.get(id=id)
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect("liststudent")


class StudentDelete(View):
    def get(self,request,*args,**kwargs):
        id=kwargs["id"]
        student=Student.objects.get(id=id)
        student.delete()
        return redirect("liststudent")





