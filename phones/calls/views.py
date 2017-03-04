from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from calls.models import PhoneCall, Employee


# Create your views here.
class EmployeeListView(ListView):
    model = Employee

class EmployeeDetailView(DetailView):
    model = Employee
