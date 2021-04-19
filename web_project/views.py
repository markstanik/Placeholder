from django.shortcuts import render
from users import models 


def homepage(request):
    return render(request, "users/homepage.html")

def about(request):
    return render(request, "users/about.html")

def results(request):
    if (request.method == "POST"):
        selectedsize=int(request.POST['selectedsize'])
        selectedmajor=request.POST['selectedmajor']
        selectedstate=request.POST['selectedstate']
        selectedprice=int(request.POST['selectedprice'])
        schools = models.Universities.objects.filter(totalstudents__lte=selectedsize).filter(state=selectedstate).filter(tuition_outstate__lte=selectedprice)
        school=schools[:10]
    return render(request, "users/listings.html", {"school": school})
