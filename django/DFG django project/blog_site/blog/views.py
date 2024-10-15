from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from blog.models import post

# Create your views here.
def blogpage(request):
    
    allposts = post.objects.all()
    context = {'allposts': allposts}
    return render(request, 'blog/blogpage.html',context)
# return HttpResponse("This is blog page will start posting soon")



def blogpost(request, slug):
    post1 = get_object_or_404(post, slug=slug)
    context = {"post": post1}
    return render(request, 'blog/blogpost.html', context)


# def blogpost(request, slug):
  
#     post1 = post.objects.filter(slug=slug)
#     context = {"post":post1}
#     return render(request, 'blog/blogpost.html',context)

      # return HttpResponse("This is BlogPOST: {slug}")