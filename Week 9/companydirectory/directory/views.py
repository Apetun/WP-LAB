from django.shortcuts import render, redirect
from .forms import WorksForm, CompanyQueryForm
from .models import Works, Lives

def index(request):
    return render(request, 'directory/index.html')

# View to insert a record into WORKS
def insert_works(request):
    if request.method == 'POST':
        form = WorksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('insert_works')  # Redirect to the same page (or elsewhere)
    else:
        form = WorksForm()
    return render(request, 'directory/insert_works.html', {'form': form})

# View to query people working for a company and the cities they live in
def query_company(request):
    results = None
    if request.method == 'POST':
        form = CompanyQueryForm(request.POST)
        if form.is_valid():
            company_name = form.cleaned_data['company_name']
            works_entries = Works.objects.filter(company_name=company_name)
            results = []
            # For each person working at the given company, try to find their city from the Lives table.
            for work in works_entries:
                try:
                    lives = Lives.objects.get(person_name=work.person_name)
                    results.append({'person_name': work.person_name, 'city': lives.city})
                except Lives.DoesNotExist:
                    results.append({'person_name': work.person_name, 'city': 'Unknown'})
    else:
        form = CompanyQueryForm()
    return render(request, 'directory/query_company.html', {'form': form, 'results': results})

