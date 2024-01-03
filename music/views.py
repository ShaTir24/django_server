from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("<h1>This is the Homepage for Music App of Demo Site!</h1>")
