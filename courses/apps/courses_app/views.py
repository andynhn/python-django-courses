# By Andy Nguyen
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course
# Create your views here.
def index(request):
    context = {
        "all_courses": Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def process(request):
    if request.method == "POST":
        errors = Course.objects.basic_validator(request.POST)
        if len(errors):
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/")
        else:
            Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
            return redirect("/")
    else:
        return redirect("/")

def destroy(request, number):
    context = {
        "course": Course.objects.get(id=number)
    }
    return render(request, 'courses_app/destroy.html', context)

def remove(request, number):
    x = Course.objects.get(id=number)
    x.delete()
    return redirect("/")