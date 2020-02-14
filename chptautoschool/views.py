from django.shortcuts import render


# from django.views.generic.base import View


# Create your views here.
def index(request):
    return render(request, "pages/index.html")


def courses(request):
    return render(request, "pages/courses.html")


def contacts(request):
    return render(request, "pages/contacts.html")


def reviews(request):
    return render(request, "pages/reviews.html")


def training(request):
    return render(request, "pages/training.html")


def useful(request):
    return render(request, "pages/useful.html")
