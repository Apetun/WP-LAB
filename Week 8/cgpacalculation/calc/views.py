from django.shortcuts import render, redirect

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        marks = request.POST.get('marks')
        
        # Store data in session
        request.session['name'] = name
        request.session['marks'] = marks
        
        # Redirect to the result page
        return redirect('result')

    return render(request, 'index.html')


def result(request):
    # Retrieve from session
    name = request.session.get('name', '')
    marks = request.session.get('marks', '0')
    
    # Convert marks to float for calculation
    try:
        total_marks = float(marks)
    except ValueError:
        total_marks = 0.0
    
    cgpa = total_marks / 50

    context = {
        'name': name,
        'cgpa': cgpa,
    }
    return render(request, 'result.html', context)
