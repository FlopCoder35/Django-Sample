from django.shortcuts import render

# Create your views here.
def Jay(request):
    print("jay file opened")
    return render(request,'maha.html')