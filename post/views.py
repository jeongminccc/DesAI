from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Result
from django.contrib.auth.decorators import login_required

def home_return(request):
    return render(request, 'home.html')

def splash_return(request):
    return render(request, 'splash.html')

def faq_return(request):
    return render(request, 'faq.html')

def team_return(request):
    return render(request, 'team.html')

def post(request):
    posts = Post.objects.all()
    return render(request, 'post.html', {'posts':posts})

@login_required
def post_detail(request, post_id):
    post_detail = get_object_or_404(Post, id=post_id)
    request_user = request.user
    comments = post_detail.comment.all()
    return render(request, 'post_detail.html', {'post':post_detail, 'user':request_user, 'comments':comments})

@login_required
def upload(request):
    user = request.user
    if request.method == 'GET':
        return render(request,'upload.html')
    elif request.method == 'POST' and user.is_authenticated:
        post = Post()
        post.title = request.POST['title']
        post.context = request.POST['context']
        post.needs = request.POST['needs']
        post.image = request.FILES['image']
        post.creator = user
        post.save()
        return redirect('/home/post/post_detail/' + str(post.id))
    else:
        return render(request, 'log_in.html')  

@login_required
def post_modify(request, post_id):
    if request.method == 'GET':
        post = get_object_or_404(Post, id = post_id)
        return render(request,'post_modify.html', {'post':post})
    elif request.method == 'POST': 
        post = get_object_or_404(Post, id=post_id)
        post.title = request.POST['title']
        post.context = request.POST['context']
        post.needs = request.POST['needs']
        post.image = request.FILES['image']
        post.creator = request.user
        post.save()
        return redirect('/home/post/post_detail/' + str(post.id))

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    post.delete()
    return redirect('/home/post/')

@login_required
def result_upload(request, post_id):
    user = request.user
    if request.method == 'GET':
        post = get_object_or_404(Post, id = post_id)
        return render(request,'result_upload.html', {'post':post})
    elif request.method == 'POST' and user.is_authenticated:
        post = get_object_or_404(Post, id = post_id)
        result = Result()
        result.post = post
        result.title = request.POST['title']
        result.creator = user
        result.image = request.FILES['image']
        result.context = request.POST['context']
        result.save()
        return redirect('/home/post/post_detail/' + str(post.id))
    else:
        return redirect('/home/post/') # 관리자 아니면 접근 x

@login_required
def result_delete(request, result_id):
    result = get_object_or_404(Result, id = result_id)
    post_id = result.post.id
    result.delete()
    return redirect('/home/post/post_detail/' + str(post_id))
    
@login_required
def result_modify(request, result_id):
    if request.method == 'GET':
        result = get_object_or_404(Result, id = result_id)
        return render(request,'result_modify.html', {'result':result})
    elif request.method == 'POST':
        result = get_object_or_404(Result, id=result_id)
        post_id = result.post.id
        result.title = request.POST['title']
        result.context = request.POST['context']
        result.image = request.FILES['image']
        result.creator = request.user
        result.save()
        return redirect('/home/post/post_detail/' + str(post_id))

@login_required
def comment_upload(request, post_id):
    user = request.user
    if request.method=='POST' and user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        comment = Comment()
        comment.post = post
        comment.creator = user
        comment.text = request.POST['context']
        comment.save()
        return redirect('/home/post/post_detail/' + str(post_id))
    else:
        return render(request, 'login.html') #로그인 안되어있으면 로그인페이지로

@login_required
def comment_delete(request, comment_id):
    comment = get_object_or_404(Comment, id = comment_id)
    post_id = comment.post.id
    comment.delete()
    return redirect('/home/post/post_detail/' + str(post_id))
    
# @login_required
# def comment_modify(request, comment_id):
#     if request.method == 'GET':
#         result = get_object_or_404(Result, id = comment_id)
#         return render(request,'result_modify.html', {'result':result})
#     elif request.method == 'POST':
#         result = get_object_or_404(Result, id=result_id)
#         post_id = result.post.id
#         result.title = request.POST['title']
#         result.context = request.POST['context']
#         result.image = request.FILES['image']
#         result.creator = request.user
#         result.save()
#         return redirect('/post/post_detail/' + str(post_id))


