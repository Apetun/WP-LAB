from django import forms
from .models import Works

# Form to insert data into WORKS
class WorksForm(forms.ModelForm):
    class Meta:
        model = Works
        fields = ['person_name', 'company_name', 'salary']

# Simple form to accept a company name for querying
class CompanyQueryForm(forms.Form):
    company_name = forms.CharField(max_length=128, label="Company Name")
