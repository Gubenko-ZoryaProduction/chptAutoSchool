from django.shortcuts import render


# from django.views.generic.base import View


# Create your views here.
def index(request):
    return render(request, "index.html")


def courses(request):
    return render(request, "courses.html")


def contacts(request):
    return render(request, "contacts.html")


def reviews(request):
    return render(request, "reviews.html")


def training(request):
    return render(request, "training.html")


def useful(request):
    return render(request, "useful.html")
