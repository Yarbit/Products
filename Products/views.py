from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext

from Products.forms import UserForm


# home page
def index(request):
    return render(request, 'index.html')


# registration page
def register(request):
    form = UserForm()
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            # creating new user
            user = User(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("login")  # move to login page
        else:
            return render(request, 'registration/registration.html', locals())
    else:
        return render(request, "registration/registration.html", locals())


def handler404(request):
    response = render_to_response('404.html')
    response.status_code = 404
    return response


def handler500(request):
    response = render_to_response('500.html')
    response.status_code = 500
    return response
