from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from Products.forms import UserForm


# home page
class Home(TemplateView):
    template_name = 'index.html'

    def get(self, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


# registration page
class Register(View):
    form_class = UserForm
    template_name = 'registration/registration.html'

    def get(self, request):
        form = self.form_class(initial={})
        return render(request, self.template_name, {'form': form})

    def post(self, request):
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

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=404)


# handler of 505
class ServerError(TemplateView):
    template_name = "500.html"

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context, status=500)
