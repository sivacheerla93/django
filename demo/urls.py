from django.urls import path
from demo.views import hello, wish, course, list_courses, prime
from demo.cookie_view import show, selectcolor, selectcity, showmovies
from demo.session_view import languages, clear
from demo.db_movies_view import city_movies
from demo.hr_views import add_dept, list_dept, list_emp, add_emp, list_all_emp, search, get_employees, get_name
from demo.ajax_views import ajax, today
from django.urls import path, re_path
import demo.orm_views as orm_views
import demo.rest_views as rest_views
import demo.class_views as class_views

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
    path('list_all_emp/', list_all_emp),
    path('ajax/', ajax),
    path('today/', today),
    path('search/', search),
    path('get_employees/', get_employees),
    re_path(r'get_emp_id/(\d+)', get_name),
    re_path(r'orm/empbydept/(\d+)', orm_views.emp_by_dept),
    path('orm/list_dept/', orm_views.list_dept),
    path('orm/list_emp/', orm_views.list_emp),
    path('orm/add_dept/', orm_views.add_dept),
    path('orm/home/', orm_views.home),
    path('orm/add_emp/', orm_views.add_emp),
    path('api/client/', rest_views.client),
    path('api/departments/', rest_views.list_dept),
    path('api/departments/<int:id>', rest_views.department_details),
    path('now/', class_views.TodayView.as_view()),
    path('deptlist/', class_views.DepartmentList.as_view()),
]
