from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.views.generic import TemplateView

from Products.forms import UserForm



# registration page
class Register(FormView):
    form_class = UserForm
    template_name = 'registration/registration.html'

    def get(self, request, **kwargs):
        form = self.form_class(initial={})
        return render(request, self.template_name, {'form': form})

    def post(self, request, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # creating new user
            user = User(username=form.cleaned_data['username'], email=form.cleaned_data['email'])
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("login")  # move to login page
        return render(request, self.template_name, {'form': form})


# handler of 404
class PageNotFound(TemplateView):
    template_name = "404.html"


# handler of 505
class ServerError(TemplateView):
    template_name = "500.html"