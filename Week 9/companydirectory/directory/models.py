from django.db import models

# Create your models here.
class Works(models.Model):
    person_name = models.CharField(max_length=128)
    company_name = models.CharField(max_length=128)
    salary = models.IntegerField()

    def __str__(self):
        return f"{self.person_name} at {self.company_name}"

class Lives(models.Model):
    person_name = models.CharField(max_length=128)
    street = models.CharField(max_length=256)
    city = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.person_name} lives in {self.city}"
