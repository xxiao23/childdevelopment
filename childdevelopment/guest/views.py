from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the guest index page.")

def vue_test(request):
    return render(request, 'guest/vue-test.html')