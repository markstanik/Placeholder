from django.shortcuts import render


def homepage(request):
    return render(request, "users/homepage.html")

def about(request):
    return render(request, "users/about.html")

def results(request):
    return render(request, "users/listings.html")
