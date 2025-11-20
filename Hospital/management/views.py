from django.shortcuts import render
from . models import Departments,Doctor
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    return render(request, 'booking.html')

def doctors(request):
    dict_docs = {
        'doctors': Doctor.objects.all()
    }
    return render(request, 'doctors.html',dict_docs)

def departments(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request, 'departments.html',dict_dept)
