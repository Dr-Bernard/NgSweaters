from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello. This is NgSwearters, where you get your best handmade sweaters for yourself and loved ones.')
    return render(request, 'hello.html', {'name': 'Ngozi'})