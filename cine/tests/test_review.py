import json
from unittest.mock import patch

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cine.models import Movie, Actor, Review  # Import your models
from cine.serializers import MovieSerializer, ActorSerializer, ReviewSerializer  # Import your serializers


# Review has : grade : integer 0-5 , movie : foreign key to Movie
class ReviewAPITestCase(APITestCase):

    @patch('cine.tasks.send_review.delay')
    def test_create_review(self, mock_delay):
        movie = Movie.objects.create(title="Test Movie", description="2023 Movie")
        data = {"grade": 4, "movie": movie.id}
        response = self.client.post(reverse("reviews-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        mock_delay.assert_called_once()

    def test_read_review(self):
        movie = Movie.objects.create(title="Test Movie", description="2023 Movie")
        review = Review.objects.create(grade=4, movie=movie)
        response = self.client.get(reverse("reviews-detail", args=[review.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), ReviewSerializer(review).data)

    def test_update_review(self):
        movie = Movie.objects.create(title="Test Movie", description="2023 Movie")
        review = Review.objects.create(grade=4, movie=movie)
        data = {"grade": 5, "movie": movie.id}
        response = self.client.put(reverse("reviews-detail", args=[review.id]), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        review.refresh_from_db()
        self.assertEqual(review.grade, 5)

    def test_delete_review(self):
        movie = Movie.objects.create(title="Test Movie", description="2023 Movie")
        review = Review.objects.create(grade=4, movie=movie)
        response = self.client.delete(reverse("reviews-detail", args=[review.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Review.objects.filter(id=review.id).exists())
