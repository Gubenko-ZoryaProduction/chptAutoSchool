from django.shortcuts import render
# from django.views.generic.base import View


# Create your views here.
def index(request):
    return render(request, "pages/index.html")
