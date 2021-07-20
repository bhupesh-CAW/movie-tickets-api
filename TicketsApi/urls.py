from django.urls import path
from .views import MovieListView, CinemaListView, BookingTicketsQuery, ShowTimeListView, PersonalDetailsView, GetShowsWithCityQuery, GetCinemasQuery

urlpatterns = [

    path('movies/', MovieListView.as_view()),
    path('cinema/', CinemaListView.as_view()),
    path('showTime/', ShowTimeListView.as_view()),
    path('user-details/', PersonalDetailsView.as_view()),
    path('getshows/', GetShowsWithCityQuery.as_view()),
    path('getcinemas/', GetCinemasQuery.as_view()),
    path('bookings/', BookingTicketsQuery.as_view()),
]

