# django defined
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import generics, status

# user-defined
from .models import Movie, Cinema, ShowTime, PersonalDetails, Booking
from .serializers import MovieSerializer, BookingDetailSerializer, CinemaSerializer, ShowTimeSerializer, PersonalDetailsSerializer, BookingSerializer, ShowMovieSerializer, CinemaShowsSerializer
# Create your views here.


class MovieListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        movies = Movie.objects.all()
        movie_name = request.query_params.get('movie_name', None)

        if movie_name is not None:
            movies = movies.filter(movie_name=movie_name)

        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, )

    def post(self, request, format=None):
        if request.user.is_superuser:
            data = JSONParser().parse(request)
            serializer = MovieSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("Error: You are not allowed to post here", status=status.HTTP_401_UNAUTHORIZED)


class CinemaListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        cinemas = Cinema .objects.all()
        cities = request.query_params.get('city', None)

        if cities is not None:
            cinemas = cinemas.filter(cinema_city=cities)
        serializer = CinemaSerializer(cinemas, many=True)
        return Response(serializer.data, )

    def post(self, request, format=None):
        if request.user.is_superuser:
            data = JSONParser().parse(request)
            serializer = CinemaSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
        return Response("Error: You are not allowed to post here", status=status.HTTP_401_UNAUTHORIZED)


class PersonalDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        details = PersonalDetails.objects.all()
        details_param = request.query_params.get('name', None)
        if details_param is not None:
            details = details.object.get(name=details_param)
        serializer = PersonalDetailsSerializer(details, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        recieved_data = JSONParser().parse(request)
        serializer = PersonalDetailsSerializer(data=recieved_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShowTimeListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        showtimes = ShowTime.objects.all()
        cinema_id = request.query_params.get('cinema_id', None)
        if cinema_id is not None:
            showtimes = showtimes.filter(cinema=cinema_id)
        movie_id = request.query_params.get('movie_id', None)
        if movie_id is not None:
            showtimes = showtimes.filter(movie=movie_id)

        serializer = ShowTimeSerializer(showtimes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        recieved_data = JSONParser().parse(request)
        cinema = Cinema.objects.get(id=recieved_data['cinema_id'])
        if recieved_data['total_seats'] > cinema.capacity:
            return Response("Select the lower no of seats", status=status.HTTP_409_CONFLICT)
        serializer = ShowTimeSerializer(data=recieved_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# From here on we have written different queries
class GetShowsWithCityQuery(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = ShowTime.objects.all()
        city_name = request.query_params.get('city', None)

        if city_name is not None:
            queryset = queryset.filter(cinema__cinema_city=city_name)

        get_movie_name = request.query_params.get('movie_name', None)

        if get_movie_name is not None:
            queryset = queryset.filter(movie__movie_name=get_movie_name)

        serializer = ShowMovieSerializer(queryset, many=True)
        return Response(serializer.data)


class GetCinemasQuery(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        queryset = Cinema.objects.all()
        get_movie = request.query_params.get('search_movie', None)
        if get_movie is not None:
            queryset = queryset.filter(
                showtimes__movie__movie_name__icontains=get_movie).distinct()
        serializer = CinemaShowsSerializer(queryset, many=True)
        return Response(serializer.data)


class BookingTicketsQuery(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        booking_id = request.query_params.get('booking_no', None)
        if booking_id is not None:
            queryset = Booking.objects.get(id=booking_id)
        else:
            return Response("invalid", status=status.HTTP_409_CONFLICT)
        seriliazer = BookingDetailSerializer(queryset)
        return Response(seriliazer.data)

    def post(self, request, format=None):
        recieve_data = JSONParser().parse(request)
        showtime = ShowTime.objects.get(id=recieve_data['show'])

        if recieve_data['quantity'] > (showtime.total_seats - showtime.booked_seats):
            return Response("Error: No seats available", status=status.HTTP_409_CONFLICT)

        recieve_data['total_amount'] = showtime.total_price * \
            recieve_data['quantity']
        showtime.booked_seats += recieve_data['quantity']
        showtime.save()

        serializer = BookingSerializer(data=recieve_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
