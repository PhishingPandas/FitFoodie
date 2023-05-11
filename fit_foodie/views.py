from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Accounts,Nutrients
from .food import nutrients

# def login(request):
#     if 'user' in request.session:

def home(request):
    login=False
    if 'user' in request.session:
        login=True
        template_name='home.html'
        context={'username': request.session['username'], 'login':login}
        return render(request,template_name,context)
    return render(request,'home.html',{'login': login})

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # print(uname, pwd)
        if Accounts.objects.filter(username=username).count()>0:
            return HttpResponse('Username already exists.')
        else:
            user = Accounts(username=username, password=password,email=email)
            user.save()
            return redirect('login')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        check_user = Accounts.objects.filter(email=email, password=password)
        if check_user:
            print("line 41")
            request.session['email'] = email
            print("line 43")
            return render(request,'home.html',{'login': True})
        else:
            return HttpResponse('Please enter valid Username or Password.')

    return render(request, 'login.html')

def logout(request):
    try:
        del request.session['user']
    except:
        return redirect('login')
    return redirect('login')

def food_input(request):
    print("line 7")
    if request.method =='POST':
        food=request.POST.get('inp')
        li=nutrients(food)
        l1=li[0]
        print("line 11")
        n=Nutrients(fname=food,fat=l1['fat'],carbohydrates=l1['carbohydrates'],cholesterol=l1['cholesterol'],protein=l1['protein'],sodium=l1['protein'])
        print("line 12")
        n.save()

        return HttpResponse('<h1>Added<h1/>')
    
    print("line 19")
    template_name='food_input.html'
    context={}
    return render(request,template_name,context)


# Create your views here.
