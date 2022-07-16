from django.shortcuts import render
from django.http import HttpResponse
import string
import datetime
from home.models import Mytext
from django.contrib import messages


# Create your views here.

def index(request):

    return render(request,"index.html")

def analyze(request):
    
    if request.method == "POST":
        djtext=request.POST.get('text','default')
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        space=" "
        analyzed=""
        antxt = request.POST.get("antxt", None)
        if antxt in ["removepunc", "removews","caps"]:
                if antxt=="removepunc":
                    for char in djtext:
                        if char not in punctuations:
                           analyzed+=char
                elif antxt=="removews":
                     for char in djtext:
                         if char not in space:
                            analyzed+=char 
                elif antxt=="caps":
                     analyzed=string.capwords(djtext)
        mytxt=Mytext(djtext=djtext,antxt=antxt,date=datetime.datetime.now())
        mytxt.save()
                      
    params={'purpose':'Your text after editing is:','analyzed_text':analyzed}
    messages.success(request, 'Your text has been edited!')
    # return HttpResponse("remove punc")
    return render(request,"analyze.html",params)
