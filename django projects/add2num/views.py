from django.shortcuts import render

# Create your views here.
def add2num(request):
    return render(request,'add2numFrm.html')
def add(request):
    val1 = int(request.POST['num1'])
    val2 = int(request.POST['num2'])
    res = val1+val2
    return render(request, 'result.html', {'result' : res})
