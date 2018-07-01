from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import datetime
from .models import Movies


def show(request):
    cookies = request.COOKIES
    if "color" in cookies:
        color = cookies["color"]
    else:
        return HttpResponseRedirect('/demo/selectcolor/')
    print(cookies)
    return HttpResponse("Your favourite color is: " + color)


def selectcolor(request):
    if request.method == "GET":
        return render(request, 'demo/selectcolor.html')
    else:
        color = request.POST['color']
        response = HttpResponseRedirect("/demo/show")
        response.set_cookie("color", color, expires=datetime.datetime.now() + datetime.timedelta(days=10))
        return response


def selectcity(request):
    if request.method == "GET":
        return render(request, 'demo/selectcity.html', {'cities': Movies.get_cities()})
    else:
        city = request.POST['city']
        response = HttpResponseRedirect("/demo/showmovies")
        response.set_cookie("city", city, expires=datetime.datetime.now() + datetime.timedelta(days=10))
        return response


def showmovies(request):
    cookies = request.COOKIES
    if 'city' in cookies:
        city = cookies['city']
    else:
        return HttpResponseRedirect("/demo/selectcity/")
    return render(request, 'demo/showmovies.html', {'city': city, 'movies': Movies.get_movies(city)})
