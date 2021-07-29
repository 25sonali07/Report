from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("Registration number")

def report(request):
    return render(request,'report.html')