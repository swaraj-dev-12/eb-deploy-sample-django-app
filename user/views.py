from django.http.response import HttpResponse

def home(request):
    return HttpResponse("hello aniket :)", 200)

def health(request):
    return HttpResponse("health ok", 200)