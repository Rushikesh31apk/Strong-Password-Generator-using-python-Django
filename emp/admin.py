from django.contrib import admin
from .models import Emp, Testomonial


# Register your models here.
class EmpAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'salary')

admin.site.register(Emp,EmpAdmin)





admin.site.register(Testomonial)