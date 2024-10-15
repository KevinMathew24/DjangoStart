from django.shortcuts import render
from django.http import HttpResponse
from blog.models import post
from home.models import Contact
from django.contrib import messages
# Create your views here.
def home(request):
    # return HttpResponse("homepage")
    return render(request,'home/home.html')

def about(request):
    return render(request,'home/about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']       
        # print(name, email, phone, content)

        if len(name)<3 or len(phone)<10 or len(email)<5 or len(content)<10:
            messages.error(request,"Please fill the form properly")

        else:    
            contact = Contact(name=name,email=email,phone=phone,content=content)
            contact.save()
            messages.success(request,"Your Response has been submitted successfully!!")
    return render(request,'home/contact.html')

# def search(request):
#     query = request.GET['query']
#     allposts = post.objects.filter(title__icontains = query)
#     output = {'allposts': allposts}
#     return render(request,'home/search.html',output)

def search(request):
    query = request.GET.get('query')
    if query:
        # Filter posts based on title or content matching the query
        results = post.objects.filter(title__icontains=query) | post.objects.filter(content__icontains=query)
    else:
        results = post.objects.none()  # Return an empty queryset if no query provided

    context = {
        'results': results,
        'query': query,
    }
    return render(request, 'home/search.html', context)
