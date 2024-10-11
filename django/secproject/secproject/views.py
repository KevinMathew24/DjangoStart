# this is created by me
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # content={
    #     "data":"Hi my name is kevin ",
    #     "roll_no" : [1,2,3,4,5,6],
    #     "variablename":"hi how are you",
    #     "firstname":"Kevin",
    #     "lastname":"Mathew"
    # }
    return render(request,"textutils2.html")

def removepunctuation(request):
    # inputtext = request.GET.get('text','default')
    # removepunctuation = request.GET.get('removepunctuation','off')
    # spaceremover = request.GET.get('spaceremover', 'off')
    # capitalize = request.GET.get('capitalize', 'off')
    # user_text

    # if removepunctuation == 'on':
    #     punctuation = '''/\,';:?!@&*.'''
    #     analyzed = ""
    #     for char in inputtext:
    #         if char not in punctuation:
    #             analyzed = analyzed + char
    #     user_text = {'task': 'Removed Punctuations', 'analyzed_text': analyzed}
    #     # return render(request,'analyzed.html', user_text)
    #     inputtext= analyzed
    
    # if spaceremover == 'on':
    #     analyzed = ""
    #     analyzed = inputtext.replace(" ", "")
    #     user_text = {'task': 'Removed Space', 'analyzed_text': analyzed}
    #     # return render(request, 'analyzed.html', user_text)
    #     inputtext= analyzed
    
    # if capitalize == 'on':
    #     analyzed = ""
    #     for char in inputtext:
    #         analyzed = analyzed + char.upper()
    #     user_text = {'task': 'Capitalized', 'analyzed_text': analyzed}
    #     # return render(request,'analyzed.html', user_text)
    #     inputtext= analyzed
    
    # if (removepunctuation != 'on' and spaceremover != 'on' and capitalize != 'on'):
    #    return HttpResponse("Plese select any one of the options.")

    # return render(request,"analyzed.html",user_text)

    # else:
    #     return HttpResponse("ERROR-YOUR TEXT HAS NOT BEEN ANALYZED")
    from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "textutils2.html")

def removepunctuation(request):
    if request.method == 'POST':
        inputtext = request.POST.get('text', 'default')
        removepunctuation = request.POST.get('removepunctuation', 'off')
        spaceremover = request.POST.get('spaceremover', 'off')
        capitalize = request.POST.get('capitalize', 'off')

        if removepunctuation == 'on':
            punctuation = '''/\,';:?!@&*.'''
            analyzed = ""
            for char in inputtext:
                if char not in punctuation:
                    analyzed += char
            user_text = {'task': 'Removed Punctuations', 'analyzed_text': analyzed}
            # return render(request, 'analyzed.html', user_text)
            inputtext= analyzed
        
        if spaceremover == 'on':
            analyzed = inputtext.replace(" ", "")
            user_text = {'task': 'Removed Space', 'analyzed_text': analyzed}
            # return render(request, 'analyzed.html', user_text)
            inputtext= analyzed
        
        if capitalize == 'on':
            analyzed = inputtext.upper()
            user_text = {'task': 'Capitalized', 'analyzed_text': analyzed}
            # return render(request, 'analyzed.html', user_text)
            inputtext = analyzed

        if (removepunctuation != 'on' and spaceremover != 'on' and capitalize != 'on'):
            return HttpResponse("Please select any one of the modes.")
        
        return render(request,"analyzed.html",user_text)
        
        
    else:
        return HttpResponse("ERROR - Only POST requests are allowed")



def capitalize(request):
    return HttpResponse("capitalize")

def spaceremover(request):
    # inputtext = request.GET.get('text', 'default')
    # spaceremover = request.GET.get('spaceremover', 'off')

    # if spaceremover == 'on' and inputtext:
    #     analyzed = inputtext.replace(" ", "")
    #     user_text = {'task': 'Removed Space', 'analyzed_text': analyzed}
    #     return render(request, 'analyzed.html', user_text)
    # else:
        return HttpResponse("hiiiii")

def about(request):
    return HttpResponse("this si about")


def home(request):
    return HttpResponse("hi welcome to home")