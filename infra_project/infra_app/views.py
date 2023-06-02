from django.http import HttpResponse


def index(request):
    return HttpResponse('I managed!')


def second_page(request):
    return HttpResponse('And this is the second page!')
