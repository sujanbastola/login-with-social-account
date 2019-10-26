# this is my owm creation
from django.http import HttpResponse
from  django.shortcuts import render
def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyze(request):
    # get the text
    djtext = request.GET.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    capital = request.GET.get('capital', 'off')
    Newlineremover = request.GET.get('Newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    print(removepunc)
    print(djtext)
    if removepunc == "on":
        analyzed =(djtext)

        punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char
        params = {'purpose': 'removed punctuations', 'analyzed_text':analyzed}
        return render(request,'home.html',params)
    elif(capital=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'change into capital', 'analyzed_text': analyzed}
        return render(request, 'home.html', params)
    elif (Newlineremover == "on"):
        analyzed = ""
        for char in djtext:
                analyzed = analyzed + char.upper()
        params = {'purpose': 'remove speace', 'analyzed_text': analyzed}
        return render(request, 'home.html', params)
    elif (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char


        params = {'purpose': 'remove speace', 'analyzed_text': analyzed}
        return render(request, 'home.html', params)
    else:
        return HttpResponse("milena hau kanxa aru hanndai gara")

def capfirst(request):
    return HttpResponse("capitalize first")

def newlineremove(request):
    return HttpResponse("newline remove first")


def spaceremove(request):
    return HttpResponse("space remover back")

def charcount(request):
    return HttpResponse("charcount ")
