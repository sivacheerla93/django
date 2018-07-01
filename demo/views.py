from django.shortcuts import render, HttpResponse
from demo.models import Course
from datetime import *
import math


# Create your views here.
def hello(request):
    if "name" in request.GET:
        name = request.GET["name"]
    else:
        name = "World!"
    return HttpResponse("<h1>Hello {}</h1>".format(name))


def wish(request):
    ct = datetime.now().time().strftime("%H")

    if ct < str(12):
        return HttpResponse("<h1>Good Morning!</h1>")
    elif ct < str(16):
        return HttpResponse("<h1>Good Afternoon!</h1>")
    elif ct < str(19):
        return HttpResponse("<h1>Good Evening!</h1>")
    else:
        return HttpResponse("<h1>Good Night!</h1>")


def course(request):
    c = Course("Angular", 3000)
    return render(request, 'demo/course.html',
                  {"course": c})


def list_courses(request):
    courses = [Course("Angular", 3000), Course("Python", 6000), Course("Java EE", 8000), Course("MS. Net", 7000)]
    return render(request, 'demo/list_courses.html', {"courses": courses})


def prime(request):
    context = dict()
    context["message"] = ""
    if request.method == "GET":
        return render(request, 'demo/prime.html', context)
    else:
        context["num"] = request.POST["num"]
        try:
            num = int(request.POST["num"])
            context["message"] = "is A Prime Number"
            for i in range(2, math.trunc(math.sqrt(num) + 1)):
                if num % i == 0:
                    context["message"] = "is Not A Prime Number!"
                    break
        except:
            context["message"] = "Sorry! Could not convert given number!!"
        return render(request, 'demo/prime.html', context)
