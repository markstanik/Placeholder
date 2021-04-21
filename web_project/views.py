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
        schools = models.Universities.objects.exclude(tuition_outstate='').filter(state=selectedstate)
        school = schools.filter(totalstudents__lte=selectedsize).filter(totalstudents__gte=600).filter(tuition_outstate__lte=selectedprice)
        school=school[:10]
        return render(request, "users/listings.html", {"school": school})
    return render(request,"users/listings.html")

def info(request):
    if (request.method=="POST"):
        num=request.POST['numID']
        college = models.Universities.objects.get(unitid=num)
        women = round((college.total_women/college.totalstudents)*100)
        black = round((college.total_black/college.totalstudents)*100)
        hispanic = round((college.total_hispanic/college.totalstudents)*100)
        pacific = round((college.total_pacific/college.totalstudents)*100)
        urban = stats(college.urbanization)
        return render(request, "users/view_info.html", {"college": college, "women": women, "black": black, "hispanic": hispanic, "pacific": pacific, "urban": urban})
    return render(request,"users/view_info.html")

def mycolleges(request):
    num=request.POST['numID']
    college = models.Universities.objects.get(unitid=num)
    women = round((college.total_women/college.totalstudents)*100)
    black = round((college.total_black/college.totalstudents)*100)
    hispanic = round((college.total_hispanic/college.totalstudents)*100)
    pacific = round((college.total_pacific/college.totalstudents)*100)
    urban = stats(college.urbanization)
    return render(request, "users/mycolleges.html", {"college": college, "women": women, "black": black, "hispanic": hispanic, "pacific": pacific, "urban": urban})
    

def stats(num):
    if num==11:
        return "City (Large)"
    elif num==12:
        return "City (Midsize)"
    elif num==13:
        return "City (Small)"
    elif num==21:
        return "Suburban (Large)"
    elif num==22:
        return "Suburban (Midsize)"
    elif num==23:
        return "Suburban (Small)"
    elif num==31:
        return "Town (Fringe)"
    elif num==32:
        return "Town (Distant)"
    elif num==33:
        return "Town (Remote)"
    elif num==41:
        return "Rural (Fringe)"
    elif num==42:
        return "Rural (Distant)"
    elif num==43:
        return "Rural (Remote)"
    return None
