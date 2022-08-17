from django.urls import path
from student import views

urlpatterns=[
    path('students/add',views.AddStudent.as_view(),name="addstudent"),
    path("",views.StudentList.as_view(),name="liststudent"),
    path("students/<int:id>", views.StudentDetail.as_view(), name="studentdetail"),
    path("students/change/<int:id>", views.ChangeStudent.as_view(), name="editstudent"),
    path("students/remove/<int:id>", views.StudentDelete.as_view(), name="deletestudent"),

]