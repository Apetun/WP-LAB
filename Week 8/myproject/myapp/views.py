from django.shortcuts import render

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")  # Not used further here but you can add validation if needed.
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        
        # You may add further validation here
        
        context = {
            "username": username,
            "email": email,
            "contact": contact,
        }
        return render(request, "success.html", context)
    
    return render(request, "register.html")

