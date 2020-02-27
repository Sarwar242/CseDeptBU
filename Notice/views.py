from django.shortcuts import render
from .models import Notice


def notices(request):
    nots = Notice.objects.all()
    return render(request, "notices.html", {'nots': nots})


def delete():
    pass