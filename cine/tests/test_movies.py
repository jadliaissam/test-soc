import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cine.models import Movie, Actor, Review  # Import your models
from cine.serializers import MovieSerializer, ActorSerializer, ReviewSerializer  # Import your serializers


class MovieAPITestCase(APITestCase):
    def test_create_movie(self):
        data = {"title": "Test Movie", "description": "Test Description"}
        response = self.client.post(reverse("movies-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_movie(self):
        movie = Movie.objects.create(title="Test Movie", description="2023 Movie")
        response = self.client.get(reverse("movies-detail", args=[movie.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), MovieSerializer(movie).data)

    def test_update_movie(self):
        movie = Movie.objects.create(title="Test Movie", description="2023 Movie")
        data = {"title": "Updated Movie", "description": "2023 Movie"}
        response = self.client.put(reverse("movies-detail", args=[movie.id]), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        movie.refresh_from_db()
        self.assertEqual(movie.title, "Updated Movie")

    def test_delete_movie(self):
        movie = Movie.objects.create(title="Test Movie", description="2023 Movie")
        response = self.client.delete(reverse("movies-detail", args=[movie.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Movie.objects.filter(id=movie.id).exists())
