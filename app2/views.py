from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def app2(request):
    return render(request,'app2.html')



def app_string(request):
    return HttpResponse('this is app_string function')