from django.http import HttpResponse


def hello(request):
    x = 1
    x += 1
    return HttpResponse("Hello")
