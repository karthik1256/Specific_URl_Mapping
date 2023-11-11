from django.shortcuts import render

# Create your views here.


def chandra(request):
    return render(request,'chandra.html')