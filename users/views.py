from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . import forms
from . import models


# Create your views here.

def test(request):
    thing="thing"
    #things = models.ExtendedUser.objects.get(firstname="jfaksdl")
    #things = models.Universities.objects.get(unitid=177834)
    thing = models.Universities.objects.filter(state="NJ")

    return render(request, "users/test.html", {"thing": thing})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, "users/login_user.html", {"form": form})


def signup_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        form2 = forms.CreateExtendedUser(request.POST)
        if form.is_valid() and form2.is_valid():
            user = form.save(commit=False)
            extendedform = form2.save(commit=False)
            user.save()
            extendedform.user = user
            extendedform.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
        form2 = forms.CreateExtendedUser()
    return render(request, "users/signup_user.html", {"form": form, "form2": form2})


def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('home')


def delete_user(request):
    try:
        request.user.extendeduser.delete()
    except Exception as e: # noqa
        request.user.organization.delete()
    request.user.delete()
    return redirect('home')


def update_info(request):
    if request.method == "POST":
        form = UserCreationForm(data=request.POST, instance=request.user)
        try:
            print("User")
            print(form.errors)
            extuser = request.user.extendeduser
            # extuser.delete()
            # request.user.delete()
            form2 = forms.CreateExtendedUser(request.POST)
            if form.is_valid() and form2.is_valid():
                request.user.username = form.cleaned_data['username']
                request.user.set_password(form.cleaned_data['password1'])
                request.user.save()
                extuser.firstname = form2.cleaned_data['firstname']
                extuser.email = form2.cleaned_data['email']
                extuser.lastname = form2.cleaned_data['lastname']
                extuser.major = form2.cleaned_data['major']
                extuser.location = form2.cleaned_data['location']
                extuser.save()
                print("Login")
                login(request, request.user)
                return redirect('home')
            else:
                return render(request, "users/update_info.html", {"form": form, "form2": form2})

        except Exception as e: # noqa
            print("ORG")
            print(form.errors)
            orguser = request.user.organization
            # orguser.delete()
            # request.user.delete()
            form2 = forms.CreateOrg(request.POST)
            if form.is_valid() and form2.is_valid():
                request.user.username = form.cleaned_data['username']
                request.user.set_password(form.cleaned_data['password1'])
                request.user.save()
                orguser.organization_name = form2.cleaned_data['organization_name']
                orguser.email = form2.cleaned_data['email']
                orguser.major = form2.cleaned_data['major']
                orguser.location = form2.cleaned_data['location']
                orguser.save()
                login(request, request.user)
                return redirect('home')
            else:
                print("INVALID")
                # form = UserCreationForm(instance=request.user)
                return render(request, "users/update_info.html", {"form": form, "form2": form2})
    else:
        form = UserCreationForm(instance=request.user)
        extuser = request.user.extendeduser
        form2 = forms.CreateExtendedUser(instance=extuser)
        return render(request, "users/update_info.html", {"form": form, "form2": form2})
        
