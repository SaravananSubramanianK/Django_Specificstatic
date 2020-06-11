from django.shortcuts import render

# Create your views here.
def saran(request):
    return render(request,'saran.html')

def sample(request):
    return render(request,'sample.html')