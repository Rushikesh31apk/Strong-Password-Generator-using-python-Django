from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from .froms import FeedbackForm
from .models import Emp, Testomonial  # Import Emp model



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


def delete_emp(request,id):
    emp = Emp.objects.get(id=id)
    emp.delete()
    return redirect('/emp/emphome/')

def update_emp(request,id):
    emp = Emp.objects.get(id=id)
    return render(request,'emp/update_emp.html',{'emp':emp})

def do_update(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        age= request.POST.get('age')
        salary = request.POST.get('salary')
        department= request.POST.get('department')
        address = request.POST.get('address')
        designation= request.POST.get('designation')
        date_of_joining = request.POST.get('date_of_joining')

        # create model object and set the data
        emp = Emp.objects.get(id=id)
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

    
    return redirect('/emp/emphome/')


def testmonials(request):
    testi= Testomonial.objects.all()

    return render(request,'emp/testmonials.html',{'testi': testi})

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            # Save the form data to the database
            testomonial = Testomonial(  # Spelling: Testomonial
                name=form.cleaned_data['name'],
                testomonial=form.cleaned_data['testomonial'],  # Spelling: testomonial
                rating=form.cleaned_data['rating'],
                image=form.cleaned_data['image']
            )
            testomonial.save()  # Spelling: testomonial
            return redirect('/emp/emphome/')  # Redirect to the home page after successful submission
        else:
            print(form.errors)  # Print form errors for debugging
    else:
        form = FeedbackForm()  # Render an empty form for GET requests

    # Always return an HttpResponse object
    return render(request, 'emp/feedback.html', {'form': form})