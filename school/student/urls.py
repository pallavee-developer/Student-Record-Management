from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('courses/',views.courses, name='courses'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('signup/',views.signup, name='signup'),
    path('viewstudents/',views.viewstudents, name='viewstudents'),
    path('registration/',views.Form_data, name='Form_data'),
    path('addcourses/', views.addcourses, name='addcourses'),
    path('addstudent/', views.addstudent, name='addstudent'),
    path('loginform/', views.loginform, name='form'),
    path('search/', views.search, ),

   
    
    
        
]