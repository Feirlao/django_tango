from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    context_dict={'boldmessage':"a,b,c,d!"}
    return render(request,'rango/index.html',context=context_dict)
def about(request):
    return HttpResponse('ABOUT')