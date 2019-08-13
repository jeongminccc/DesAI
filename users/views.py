from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from .models import User

def log_home(request):
    return render(request, 'log_home.html')

def signup(request):   
    #get방식으로 접속
    if request.method == 'GET':
        return render(request, 'sign_up.html', {'form':auth.forms.UserCreationForm()})
    #post방식으로 접속
    else: #method == "POST":
        form = auth.forms.UserCreationForm(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password1'],
                name = request.POST.get('name'),
                email = request.POST.get('email')
                )
            user.save() #저장함
            auth.login(request, user)
            print("Signup Success")
            return render(request, 'home.html', {}) #메인페이지로 이동
        else:
            print("Signup Failed")
            return render(request, 'sign_up.html', {'form':auth.forms.UserCreationForm()}) #다시 회원가입으로


def login(request):
    if request.method == 'GET':
        print("method GET")
        return render(request, 'log_in.html', {})
    else: #method == "POST":
        form = auth.authenticate(username = request.POST['username'], password = request.POST['password'])
        if form is not None:
            auth.login(request, form)
            print("Login Success")
            return render(request, 'home.html', {})  
        else:
            print("Login Failed")
            return render(request, 'log_in.html', {})

def logout(request):
    auth.logout(request)
    print("Logout Success")
    return redirect('/')

def mypage(request):
    user = request.user
    posts = user.post.all()
    a = 0
    b = 0
    c = 0
    for post in posts:
      c = post.result.count()
      if c == 0: #진행중
          b += 1
      else: #완료 ( 답변카운트 ++ )
          a += 1
    return render(request, 'mypage.html', {'user':user, 'posts':posts, 'a':a, 'b':b})

def mypage_update(request, user_id):
    user = get_object_or_404(User, pk = user_id)
    return render(request, 'mypage_update.html', {'user' : user})

def about(request):
    return render(request, 'about.html')
