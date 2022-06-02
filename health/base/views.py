from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from base.models import *
from django.views.generic.edit import CreateView, FormView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# Create your views here.


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')

class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(RegisterPage, self).get(*args, **kwargs)


def home(request):
    obj=Doctor.objects.all()
    context={
        "obj":obj
    }
    return render(request,"base/home.html",context)

class Hospital_card(LoginRequiredMixin,CreateView):
    model = Hospital_card
    fields = ['full_name','age','email','residence','with_insurance','id_type','id_number','is_valid']
    template_name = 'base/hospital_card.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Hospital_card, self).form_valid(form)

class Complaint(LoginRequiredMixin,CreateView):
    model = Complaint
    fields = ['name','description']
    template_name = 'base/complaint.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Complaint, self).form_valid(form)