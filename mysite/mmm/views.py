#from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from .models import GymLocation
#from .forms import GymCreatForm
from .forms import GymLocationCreateForm 
from django.db.models import Q
from django.views.generic import DetailView, CreateView, UpdateView
# from profiles.tasks import sleepy





class GymListView(LoginRequiredMixin, ListView):
    template_name = 'Gym/Gym_list.html'
    def get_queryset(self):
        # sleepy(10)
        return GymLocation.objects.filter(owner=self.request.user)
    


class GymDetailView(LoginRequiredMixin, DetailView):
    template_name = 'Gym/gymlocation_detail.html'
    def get_queryset(self):
        return GymLocation.objects.filter(owner=self.request.user)
    


class GymCreateView(LoginRequiredMixin, CreateView):
    form_class = GymLocationCreateForm
    template_name = "forms.html"
    login_url = '/login/'
    #success_url = ("/Gym/")
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(GymCreateView, self).form_valid(form)

    def get_context_data(self,*args, **kwargs):
        context = super(GymCreateView, self).get_context_data(*args, **kwargs)
        context['title']= 'Add Gym'
        return context

class GymUpdateView(LoginRequiredMixin, UpdateView):
    form_class = GymLocationCreateForm
    template_name = "Gym/detail-update.html"
    login_url = '/login/'
    def get_context_data(self,*args, **kwargs):
        context = super(GymUpdateView, self).get_context_data(*args, **kwargs)
        name = self.get_object().name
        context['title']= f'Update gym: {name}'
        return context
    def get_queryset(self):
        return GymLocation.objects.filter(owner_id=self.request.user)
    