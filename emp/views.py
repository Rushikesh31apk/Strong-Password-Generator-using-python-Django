from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


# Create your views here.
def emp_home(request):
    return render(request,'emp/index.html',{})

def add_emp(request):
    if request.method == 'POST':
        return redirect('/emp/emphome/')


    return render(request,'emp/add_emp.html',{})