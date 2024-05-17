from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.

def main(request):
    return render(request, 'main.html')

def reg(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        mail = request.POST['mail']
        psw = request.POST['psw']
        cpsw = request.POST['cpsw']

        if psw == cpsw:
            if User.objects.filter(username=username).exists():
                # print('username already taken!')
                messages.info(request, 'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=mail).exists():
                # print('mail already taken')
                messages.info(request, 'Email Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username = username, password = psw, email = mail, first_name = fname, last_name = lname)
                user.save()
                print('user created')
                return redirect('login')
        else:
            print('password not matching!')
            messages.info(request, 'password is not matching')
            return redirect('register')

    else:
        return render(request, 'reg.html')

def log(request):
    if request.method == 'POST':
        username = request.POST['username']
        psw = request.POST['password']
        user = auth.authenticate(username = username, password = psw)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials')
            return redirect('/')

    else:
        return render(request, 'login.html')


