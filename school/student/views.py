from django.shortcuts import render, redirect
from . models import *
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.db.models import Q

# Create your views here.
def index(request):
    return render(request, 'index.html')


def courses(request):
    course = Addcourse.objects.all()
    return render(request, 'courses.html', {'course': course})


def signup(request):
    return render(request, 'sign-up.html')


def dashboard(request):
    addcourses = Addcourse.objects.all()
    totalcourse = Addcourse.objects.all().count()
    totalstudent = AddStudents.objects.all().count()
    return render(request, 'dashboard.html', {'addcourses': addcourses, 'totalcourse': totalcourse, 'totalstudent': totalstudent})


def viewstudents(request):
    stu = AddStudents.objects.all()
    addcourses = Addcourse.objects.all()
    redirect("/viewstudents/")
    return render(request, 'viewstudents.html', {'stu': stu, 'addcourses': addcourses})


def Form_data(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        if Formdata.objects.filter(email=email).exists():
            messages.error(request, "Email already Exist")
            return redirect('/signup')
        else:
            Formdata.objects.create(name=name, email=email, password=password)
            messages.success(request, 'Registration successful')
            return redirect('/')


def loginform(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        if Formdata.objects.filter(email=email).exists():
            obj = Formdata.objects.get(email=email)
            password = obj.password
            if check_password(password, password):
                return redirect('/dashboard/')
            else:
                messages.error(request, 'Password incorrect')
                return redirect('/')
        else:
            messages.error(request, 'Email is not registered')
            return redirect('/')


# def loginform(request):
#     if request.method=='POST':
#         username = request.POST['email']
#         pwd = request.POST['password']
#         users = authenticate(email=username, password=pwd)
#         if users is not None:
#             login(request, users)
#             return redirect('/dashboard')
#         else:
#             return redirect('/')
#     else:
#         return redirect('/')

def addcourses(request):
    if request.method == 'POST':
        c_name = request.POST['CourseName']
        c_fees = request.POST['CourseFees']
        c_duration = request.POST['CourseDuration']
        c_desc = request.POST['CourseDesc']
        messages.success(request, 'Course Added Successfully')
        Addcourse.objects.create(
            course=c_name, fees=c_fees, duration=c_duration, desc=c_desc)
        return redirect('/courses/')


def addstudent(request):
    if request.method == "POST":
        stu_name = request.POST.get("Name")
        stu_email = request.POST.get("Email")
        stu_mobile = request.POST.get("Mobile")
        stu_college = request.POST.get("College")
        stu_degree = request.POST.get("Degree")
        stu_address = request.POST.get("Address")
        stu_addcourse_id = request.POST.get("course")
        total_amount = request.POST.get("qty")
        paid_amount = request.POST.get("cost")
        due_amount = request.POST.get("DueAmount")
        stu_course = Addcourse.objects.get(id=stu_addcourse_id)
        if AddStudents.objects.filter(semail=stu_email).exists():
            messages.error(request, "Email id already exists")
            return redirect('addstudent')

        elif AddStudents.objects.filter(smobile=stu_mobile).exists():
            messages.error(request, "Mobile Number already exists")
            return redirect('addstudent')
        else:
            AddStudents.objects.create(sname=stu_name,
                                       semail=stu_email,
                                       smobile=stu_mobile,
                                       scollege=stu_college,
                                       sdegree=stu_degree,
                                       saddress=stu_address,
                                       scourse=stu_course,
                                       total_amount=total_amount,
                                       paid_amount=paid_amount,
                                       due_amount=due_amount,
                                       )
            messages.success(request, "Student Added Successfully!!")
            stu = AddStudents.objects.all()
            addcourses = Addcourse.objects.all()
            return render(request, 'viewstudents.html', {'stu': stu, 'addcourses': addcourses, })

    else:
        stu = AddStudents.objects.all()
        addcourses = Addcourse.objects.all()
        return render(request, 'viewstudents.html', {'stu': stu, 'addcourses': addcourses})
# Students Search Funcation
def search(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(sname__icontains=q) | Q(
            semail__icontains=q)) | Q(smobile__icontains=q)
        stu = AddStudents.objects.filter(multiple_q)
    else:
        stu = AddStudents.objects.all()
    context = {
        'stu': stu
    }
    return render(request, 'viewstudents.html', context)