#this file created by me

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
import random

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