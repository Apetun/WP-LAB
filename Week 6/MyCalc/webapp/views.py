from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request,'basic.html')


def calculate(request):
    result = None
    if request.method == "POST":
        try:
            num1 = int(request.POST.get("number1"))
            num2 = int(request.POST.get("number2"))
            operation = request.POST.get("operation")
            
            if operation == "add":
                result = num1 + num2
            elif operation == "subtract":
                result = num1 - num2
            elif operation == "multiply":
                result = num1 * num2
            elif operation == "divide":
                if num2 != 0:
                    result = num1 / num2
                else:
                    result = "Division by zero error"
            else:
                result = "Invalid operation selected"
        except ValueError:
            result = "Please enter valid integers."
    
    return render(request, "basic.html", {"result": result})

