from django.shortcuts import render

# Create your views here.
def homefn(request):
    return render(request,'contact.html')
def detailfn(request):
    return render(request,'detail.html')    