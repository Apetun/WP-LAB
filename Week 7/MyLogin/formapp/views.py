from django.shortcuts import render
from .forms import LoginForm

def home_view(request):
    username = "not logged in"
    contact_num = "not found"
    
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            contact_num = form.cleaned_data.get('contact_num')
    else:
        form = LoginForm()
    
    context = {
        'username': username,
        'contact_num': contact_num,
        'form': form,
    }
    
    return render(request, 'login.html', context)

