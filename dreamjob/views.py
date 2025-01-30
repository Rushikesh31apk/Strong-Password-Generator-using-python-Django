#this file created by me

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import random
# date time import
from datetime import datetime

def index(request):
    return  render(request,'index.html')
def password(request):
    length=request.GET.get('length')
    isUpper=request.GET.get('use_uppercase')
    isNumber=request.GET.get('use_numbers')
    isSymbol=request.GET.get('use_symbols')

    choices_I_have=list('abcdefghijklmnopqrstuvwxyz')
    if isUpper=='on':
        choices_I_have.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
    if isNumber=='on':
        choices_I_have.extend(list('0123456789'))
    if isSymbol=='on':
        choices_I_have.extend(list('!@#$%^&*_+-=:?'))
    myPassword=""
    for i in range(int(length)):
        choosen=random.choice(choices_I_have)
        myPassword+=choosen
    
    data={
        'password':myPassword
    }

    return render(request,'password.html',data)
def home(request):
    data_submited = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        msg = request.POST.get('message')  # Correct variable name

        if name and email and msg:
            data_submited = True

        print('Response:')
        print(f'{{\n\tname: {name},\n\temail: {email},\n\tmessage: {msg}\n}}\n')  # Use msg instead of message

    
    
    date=datetime.now()
    isActive=True
    student={
        'name':'Rushikesh',
        'age':20,
        'roll':1,
        'city':'Pune',
    }
    name='Rushikesh Narawade'
    programs=[
        'write program to find prime number',
        'write program to find factorial of a number',
        'write program to find fibonacci series',
        'write program to find palindrome number',
        'write program to find armstrong number',
    ]
    data={
        'isActive':isActive,
        'name':name,
        'date':date,
        'isActive':isActive,
        'student':student,
        'programs':programs,
        'data_submited':data_submited
    }
    return render(request,'home.html',data)

