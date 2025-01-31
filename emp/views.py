from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .models import Emp  # Import Emp model



# Create your views here.
def emp_home(request):
    emp=Emp.objects.all()

    return render(request,'emp/index.html',{'emp':emp})

def add_emp(request):
    if request.method == 'POST':
        # data fetch
        name = request.POST.get('name')
        email = request.POST.get('email')
        age= request.POST.get('age')
        salary = request.POST.get('salary')
        department= request.POST.get('department')
        address = request.POST.get('address')
        designation= request.POST.get('designation')
        date_of_joining = request.POST.get('date_of_joining')


        # create model object and set the data
        emp = Emp()
        emp.name = name
        emp.email = email
        emp.age = age
        emp.salary = salary
        emp.department = department
        emp.address = address
        emp.designation= designation
        emp.date_of_joining = date_of_joining

        # save the data to database
        emp.save()

        # prepare msg to be displayed on the page
        return redirect('/emp/emphome/')


    return render(request,'emp/add_emp.html',{})