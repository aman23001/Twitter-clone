from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Post
from .forms import  PostForm

# Create your views here.

def index(request):
    

    if request.method=='POST':

        form = PostForm(request.POST,request.FILES)
        

        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.erros.as_json())
    posts = Post.objects.all().order_by('-created_at')[:20] 


    return render(request,'posts.html',
                 {'posts': posts})



def delete(request, post_id):
    post=Post.objects.get(id=post_id)
    post.delete()
    return HttpResponseRedirect("/")
def edit(request, post_id):
    # Find post
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    form = PostForm
    # form = PostForm

    # show
    return render(request, 'edit.html', {'post': post, 'form': form})


# function for the like button for our posts
def LikeView(request, post_id):
    new_value = Post.objects.get(id=post_id)
    new_value.likes += 1
    new_value.save()
    return HttpResponseRedirect('/')   