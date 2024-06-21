from django.shortcuts import render
from django.http import HttpResponse
from crud.models import Classroom

# Create your views here.

def home_view(request):
    return HttpResponse("<h1> This is from Home Page</h1>")

def another_home_view(request):
    return HttpResponse("<h1> This is from Another Page</h1>")

def rootPageView(request):
    return render(request,template_name="myapp/root_page.html")

def portfolio_view(request):
    return render(request,template_name="portfolio/index.html")

def learning_dtl_view(request):
    c={"name":"Prashiddha Joshi","Student":"Ram"}
    s=[
        {"name": "Jon", "age": "12","display":True},
        {"name": "Jonny", "age": "22","display":False},
        {"name": "Tom", "age": "32","display":True},
        {"name": "Tommy", "age": "92","display":False},

    ]
    c.update(students=s)
    #context should always be dict
    return render(request,template_name="myapp/dtl.html",context=c)

def using_bootstrap_view(request):
    s = [
        {"name": "Jon", "age": "12", "display": True, "email": "jon@gmail.com", "address": "Ktm"},
        {"name": "Jonny", "age": "22", "display": False, "email": "jonny@gmail.com", "address": "Pkr"},
        {"name": "Tom", "age": "32", "display": True, "email": "tom@gmail.com", "address": "Bkt"},
        {"name": "Tommy", "age": "92", "display": False, "email": "tommy@gmail.com", "address": "Ltp"},
    ]
    
    return render(request, template_name="myapp/using_bootstrap.html", context={"students": s})


def temp_inherit_view(request):
    classrooms = Classroom.objects.all()
    return render(request,template_name="myapp/home.html",context={"classrooms":classrooms})

def about_view(request):
        return render(request,template_name="myapp/about.html")


def contact_view(request):
        return render(request,template_name="myapp/contact.html")

#features from DTL
#{% load static %}
#{% url '' %}
#{% static 'stati/path' %}
#{{name}}