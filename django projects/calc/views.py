from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    msg = "<h1>Welcome to Vinsup</h1>"
    return HttpResponse(msg)
def index(request):
    msg = "<b>This is index page</b>"
    return HttpResponse(msg)
def dtl_test(request):
    data = {
        'name' : "Azar",
        'age' : 22,
        'city' : 'Madurai'
    }
    # return render(request,'home.html',{'name' : "Azarudeen"})
    return render(request,'home.html',
                  { 'name' : "Azar",
                    'age' : 22,
                    'city' : 'Madurai'
    })
