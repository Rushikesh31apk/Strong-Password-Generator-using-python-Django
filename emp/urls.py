from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('emphome/',views.emp_home),
   path('add-emp/',views.add_emp),
   path('delete-emp/<int:id>',views.delete_emp),
   path('update-emp/<int:id>',views.update_emp),
   path('do-update-emp/<int:id>',views.do_update),
   path('testmonials/',views.testmonials),
]