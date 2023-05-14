from django.db import models
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')

# Create your models here.
class Addcourse(models.Model):
    course=models.CharField(max_length=20)
    fees=models.IntegerField()
    duration=models.CharField(max_length=100)
    desc=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.course
    
class Formdata(models.Model):
    name= models.CharField(max_length=20)
    email= models.EmailField( max_length=254)
    password=models.CharField(max_length=256)
    
    
class AddStudents(models.Model):
    sname = models.CharField(max_length=100,blank=True, null=True, validators=[alphanumeric])
    semail = models.EmailField(max_length=100)
    smobile = models.CharField(max_length=10)
    saddress= models.CharField(max_length=255)
    scollege = models.CharField(max_length=255)
    sdegree = models.CharField(max_length=100)
    total_amount = models.IntegerField()
    paid_amount = models.IntegerField()
    due_amount = models.FloatField()
    scourse= models.ForeignKey(Addcourse, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.sname