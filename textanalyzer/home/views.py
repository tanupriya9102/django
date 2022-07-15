from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):

    return render(request,"index.html")

def analyze(request):
    
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    print(removepunc)
    # analyzed=djtext
    punctuations='''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''
    analyzed=""
    for char in djtext:
        if char not in punctuations:
            analyzed+=char


   
    params={'purpose':'After Removing punctuations:','analyzed_text':analyzed}
    # return HttpResponse("remove punc")
    return render(request,"analyze.html",params)
