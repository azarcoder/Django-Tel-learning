from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.
def index(request):
    if request.method == 'POST':
        num1 = float(request.POST['num1'])
        num2 = float(request.POST['num2'])
        operation = request.POST['operation']
        if operation == 'add':
            result = num1 + num2
        elif operation == 'sub':
            result = num1 - num2
        elif operation == 'mul':
            result = num1 * num2
        elif operation == 'div':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Cannot divide by zero"
        else:
            result = "Invalid operation"
        return render(request, 'calculator.html', {'result' : result})
    else:
        return render(request, 'calculator.html')

