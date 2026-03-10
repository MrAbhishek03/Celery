from unittest import result
from celery.result import AsyncResult
from django.shortcuts import render
from .tasks import add,sub

# Create your views here.
# 

def index(request):
    result1=add.apply_async(args=[10,2])
    # result2=sub.apply_async(args=[40,36])
    print("-*"*20)
    print(f"results page: {result1}")
    print(f"results state: {result1.state}")
    print(f"results status: {result1.status}")
    print("-*"*20)

    # print(f"results2 page: {result2}")
    # print(f"results2 state: {result2.state}")
    # print(f"results2 status: {result2.status}")
    # print("-*"*20)
    return render(request, 'home.html', {'result1': result1, 'result2': result2} )

def about(request):
    print("about page: ")
    return render(request, 'about.html')

# def results(request):
#     result=add.delay(4, 6)
#     print("-*"*20)
#     print(f"results page: {result}")
#     print(f"results state: {result.state}")
#     print(f"results status: {result.status}")
#     print("-*"*20)
#     return render(request, 'result.html', {'result': result}    )


def results(request,id):
    result = AsyncResult(id)
    return render(request, 'result.html', {'result': result}    )