from django.contrib import admin
from .models import Cinema, Movie, ShowTime, PersonalDetails
# Register your models here.
admin.site.register(Movie)
admin.site.register(Cinema)
admin.site.register(ShowTime)
admin.site.register(PersonalDetails)
