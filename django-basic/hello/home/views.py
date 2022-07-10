from django.shortcuts import render,HttpResponse
from matplotlib.style import context

# Create your views here.

def index(request):
    context={
        "variable":"this is variable"
    }
    return render(request,"index.html",context)
    # return render(request,"index.html")

def about(request):
    return HttpResponse("this is About page!!")

def contact(request):
    return HttpResponse("this is Contact page!!")

