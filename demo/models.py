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


# For ORM using MySQL
class DBCourse(models.Model):
    title = models.CharField(max_length=20)
    duration = models.IntegerField()
    fee = models.IntegerField()

    def __str__(self):
        return self.title


class DBStudent(models.Model):
    fullname = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    course = models.ForeignKey('DBCourse', on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname


class Person(models.Model):
    fullname = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    mobile = models.CharField(max_length=10)

    def __str__(self):
        return self.fullname

        # To rename table name

    class Meta:
        db_table = 'Persons'


class Department(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Departments"


class Employee(models.Model):
    fullname = models.CharField(max_length=50)
    salary = models.IntegerField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

    class Meta:
        db_table = 'Employees'
