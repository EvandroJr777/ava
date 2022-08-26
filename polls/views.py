from django.http import HttpResponse


def index(request):
    return HttpResponse("oi")

# Create your views here.
