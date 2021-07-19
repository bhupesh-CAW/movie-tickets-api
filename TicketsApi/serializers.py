from rest_framework import serializers
from .models import Movie, Cinema, ShowTime, PersonalDetails, Booking
# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cinema
        fields = '__all__'


class ShowTimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShowTime
        fields = '__all__'


class PersonalDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalDetails
        fields = '__all__'


class ShowMovieSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer()
    movie = MovieSerializer()

    class Meta:
        model = ShowTime
        fields = ('id', 'show_start_time', 'show_end_time',
                  'total_seats', 'booked_seats', 'cinema', 'movie')


class CinemaShowsSerializer(serializers.ModelSerializer):
    showtimes = ShowMovieSerializer(many=True)

    class Meta:
        model = Cinema
        fields = ('id', 'cinema_name', 'cinema_address',
                  'cinema_city', 'showtimes')


class BookingSerializer(serializers.ModelSerializer):
    show = ShowMovieSerializer()
    details = PersonalDetailsSerializer()

    class Meta:
        model = Booking
        fields = ('id', 'total_amount', 'quantity', 'details', 'show')



class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'total_amount', 'quantity', 'details', 'show')
