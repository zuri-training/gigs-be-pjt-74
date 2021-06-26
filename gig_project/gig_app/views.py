from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView


class Register(CreateView):
    form_class= UserCreationForm
    template_name='registration/register.html'
    success_url= reverse_lazy('success')

def Success(request):
    return HttpResponse('DONE')
