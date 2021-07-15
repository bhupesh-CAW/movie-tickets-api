from django.db import models

# Create your models here.


class Movie(models.Model):
    movie_name = models.CharField(max_length=50, unique=True)
    movie_genre = models.CharField(max_length=25)
    movie_cast = models.TextField()
    movie_duration = models.FloatField(null=False)
    release_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.movie_name


class Cinema(models.Model):
    cinema_name = models.CharField(max_length=50, null=False)
    cinema_address = models.TextField()
    cinema_city = models.CharField(max_length=50, null=False)
    capacity = models.IntegerField(null=False)

    def __str__(self) -> str:
        return self.cinema_name


class ShowTime(models.Model):
    cinema = models.ForeignKey(Cinema, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    booked_seats = models.IntegerField(null=False)
    show_start_time = models.DateTimeField(auto_now_add=True)
    show_end_time = models.DateTimeField(auto_now_add=True)
    total_seats = models.IntegerField(null=False)
    total_price = models.FloatField(null=False)

    def __str__(self) -> str:
        return self.total_price


class PersonalDetails(models.Model):
    person_name = models.CharField(max_length=20, null=False)
    person_email = models.CharField(max_length=20, null=False)

    def __str__(self) -> str:
        return self.person_name


class Booking(models.Model):
    details = models.ForeignKey(PersonalDetails, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    total_amount = models.IntegerField(null=False)
    show = models.ForeignKey(ShowTime, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.total_amount
