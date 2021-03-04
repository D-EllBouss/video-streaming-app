from django.http import JsonResponse, HttpResponse, HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegistrationForm, UserForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from series.variables import *
from series.views import *
from series.urls import *


# Create your views here.
def user_login(request):

    login_form = LoginForm(request.POST)
    if login_form.is_valid():
        cd = login_form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password'])
        if user:
            login(request, user)
            return redirect('series:index')
        else:
            return HttpResponse("Sorry. Your username or password is not right.")
    else:
        return HttpResponse("Invaild login")


def register(request):

    user_form = RegistrationForm(request.POST)
    if user_form.is_valid():
        new_user = user_form.save(commit=False)
        new_user.set_password(user_form.cleaned_data['password'])
        new_user.save()
        login(request, new_user)
        return redirect('series:index')
    else:
        return HttpResponse("sorry, your can not register.")


def profile(request):

    return render(request, "series/profile.html",
                  {
                      'series_all': series_all,
                      'GENRE_CHOICES': GENRE_CHOICES
                  }
                  )
