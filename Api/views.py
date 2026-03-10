from unittest import result
from celery.result import AsyncResult
from django.shortcuts import render
from .tasks import add,sub

# Create your views here.
# 

def index(request):
    result1=add.apply_async(args=[10,2])
    
    print("-*"*20)
    print(f"results page: {result1}")
    print(f"results state: {result1.state}")
    print(f"results status: {result1.status}")
    print("-*"*20)

    
    return render(request, 'home.html', {'result1': result1, 'result2': result2} )

def about(request):
    print("about page: ")
    return render(request, 'about.html')

def home_page(request):
    print("about page: ")
    return render(request, 'about.html')


def results(request,id):
    result = AsyncResult(id)
    return render(request, 'result.html', {'result': result}    )