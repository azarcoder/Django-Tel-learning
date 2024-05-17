from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'register.html')

def regis(request):
    name = request.POST['name']
    password = request.POST['psw']
    address = request.POST['addr']
    mail = request.POST['mail']
    print(name,password,address,mail)
    return render(request, 'registerdetails.html',{'name':name, 'password':password, 'address':address,'mail':mail})
