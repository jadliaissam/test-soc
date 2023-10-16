from django.contrib import admin

# Register your models here.

from cine.models import Movie, Actor, Review

admin.site.register(Movie)
admin.site.register(Actor)
admin.site.register(Review)
