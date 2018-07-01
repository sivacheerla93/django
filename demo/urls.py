from django.urls import path
from demo.views import hello, wish, course, list_courses, prime
from demo.cookie_view import show, selectcolor, selectcity, showmovies
from demo.session_view import languages, clear
from demo.hr_views import add_dept
from demo.db_movies_view import city_movies
from demo.hr_views import add_dept, list_dept, list_emp, add_emp
from django.urls import path, re_path

urlpatterns = [
    path('hello/', hello),
    path('wish/', wish),
    path('course/', course),
    path('list_courses/', list_courses),
    path('prime/', prime),
    path('show/', show),
    path('selectcolor/', selectcolor),
    path('selectcity/', selectcity),
    path('showmovies/', showmovies),
    path('languages/', languages),
    path('languages/clear/', clear),
    path('add_dept/', add_dept),
    path('city_movies/', city_movies),
    path('add_dept/', add_dept),
    path('list_dept/', list_dept),
    re_path(r'list_emp/(\d+)', list_emp),
    path('add_emp/', add_emp),
]
