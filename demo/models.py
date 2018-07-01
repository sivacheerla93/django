from django.db import models


# Create your models here.
class Course:
    def __init__(self, name, fee):
        self.name = name
        self.fee = fee

    def __str__(self):
        return "Courser: %s, Fee: %d" % (self.name, self.fee)


class Movies:
    movies = {
        'Vizag': ["Rangasthalam", "Bharat Ane Nenu", "Tholiprema"],
        'Hyderabad': ["Rangasthalam", "Bharat Ane Nenu", "Tholiprema", "Gladiator"],
        'Chennai': ["Rangasthalam", "Bharat Ane Nenu", "Tholiprema", "Robot 2"],
        'Mumbai': ["Secret super star", "Raabta", "Hindi Medium"]
    }

    @staticmethod
    def get_cities():
        return Movies.movies.keys()

    @staticmethod
    def get_movies(city):
        return Movies.movies[city]
