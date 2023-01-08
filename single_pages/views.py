from django.shortcuts import render, get_object_or_404

from blog.forms import CommentForm
from blog.models import Post
from django.shortcuts import render, redirect

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied




# Create your views here.
def landing(request):
    recent_post = Post.objects.order_by('-pk')[:3] # 0,1,2 까지만 가져오겠다.
    return render(request, 'single_pages/landing.html', {
        'recent_posts' : recent_post,
    })



def Ear(request):
    return render(request, 'single_pages/Ear.html')

def new_comment(request,pk):
    if request.user.is_authenticated:
        post = get_object_or_404(Post,pk=pk) # POST를 가져온다.

        if request.method == 'POST': # submit 버튼을 클릭하면 POST 방식으로 전달이 된다.
            comment_form = CommentForm(request.POST)
            if request.method == 'POST':
                comment_form = CommentForm(request.POST) # POST 방식으로 서버에 요청이 들어왔다면
                # POST 방식으로 들어온 정보를 CommentForm의 형태로 가져온다.
                if comment_form.is_valid():
                    comment = comment_form.save(commit=False)
                    comment.post = post
                    comment.author = request.user
                    comment.save() # commnet라는 객체는 서버에 있는 모델에 저장이 된다.
                    return redirect(post.get_absolute_url())
        else: #GET으로 들어왔다면
            return redirect(post.get_absolute_url())
    else:
        raise PermissionDenied