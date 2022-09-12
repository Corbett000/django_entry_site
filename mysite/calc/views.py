from django.http import HttpResponse


def index(request):
    return HttpResponse("Have a great GHW!")