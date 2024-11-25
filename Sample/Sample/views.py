from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("Hello, u are at home page")
    return render(request,'index.html')
def about(request):
    return HttpResponse("Hello , u are at about page ")
def contact(request):
    return HttpResponse("Hello, u are at contact page")
