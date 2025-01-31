from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('emphome/',views.emp_home),
   path('add-emp/',views.add_emp),
]