from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import mysql.connector


def city_movies(request):
    con = mysql.connector.connect(host="localhost", user="root", password="9866850403", database="python")
    cur = con.cursor()
    cur.execute("select * from cities")

    cities = [row[1] for row in cur.fetchall()]

    movies = []
    city = ""
    if request.method == "POST":
        city = request.POST["city"]
        print(city)
        cur.execute("select Code from cities where Name = '{}'".format(city))
        Code = cur.fetchone()
        City_Code = Code[0]
        cur.execute("select * from movies where City = {}".format(City_Code))
        movies = [row[1] for row in cur.fetchall()]
        print(movies)

    cur.close()
    con.close()

    return render(request, 'demo/city_movies.html', {'cities': cities, 'movie_city': movies, 'city_name': city})
