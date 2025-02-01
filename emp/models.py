from django.db import models

# Create your models here.
class Emp(models.Model):
    name = models.CharField(max_length=100)
    mail= models.EmailField(max_length=100)
    designation = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    department = models.CharField(max_length=100)
    date_of_joining = models.DateField()

    def __str__(self):
        return self.name


    
from django.db import models

from django.db import models

class Testomonial(models.Model):  # Spelling: Testomonial
    name = models.CharField(max_length=100)
    testomonial = models.TextField()  # Spelling: testomonial
    image = models.ImageField(upload_to='testomonial/')  # Spelling: testomonial
    rating = models.IntegerField()  # Removed max_length (not valid for IntegerField)

    def __str__(self):
        return self.testomonial  # Spelling: testomonial