from django.shortcuts import render
from .models import Students,trainer,course

# Create your views here.
def homepage(request):
    total_students = Students.objects.all().count()
    total_courses = course.objects.all().count()
    total_trainers = trainer.objects.all().count()
    context = {
        'total_courses' :total_courses,
        'total_students' : total_students,
        'total_trainers' : total_trainers
    }
    return render(request,'academy/homepage.html',context)

def courses(request):
    total_courses = course.objects.all()
    context = {
        'courses':total_courses
    }
    return render(request,'academy/course.html',context)

def trainers(request):
    total_trainers = trainer.objects.all()
    context = {
        'trainers':total_trainers
    }
    return render (request,'academy/trainer.html',context)
def student(request):
    total_students = Students.objects.all()
    context = {
        'students':total_students
    }
    return render (request,'academy/students.html',context)