import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from cine.models import Movie, Actor, Review  # Import your models
from cine.serializers import MovieSerializer, ActorSerializer, ReviewSerializer  # Import your serializers


# actor has : firstName, lastName and movies : many to many to Movie
class ActorAPITestCase(APITestCase):
    def test_create_actor(self):
        data = {"first_name": "Test Actor", "last_name": "Test Actor"}
        response = self.client.post(reverse("actors-list"), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_actor(self):
        actor = Actor.objects.create(first_name="Test Actor", last_name="Test Actor")
        response = self.client.get(reverse("actors-detail", args=[actor.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), ActorSerializer(actor).data)

    def test_update_actor(self):
        actor = Actor.objects.create(first_name="Test Actor", last_name="Test Actor")
        data = {"first_name": "Updated Actor", "last_name": "Updated Actor"}
        response = self.client.put(reverse("actors-detail", args=[actor.id]), data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        actor.refresh_from_db()
        self.assertEqual(actor.first_name, "Updated Actor")

    def test_delete_actor(self):
        actor = Actor.objects.create(first_name="Test Actor", last_name="Test Actor")
        response = self.client.delete(reverse("actors-detail", args=[actor.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Actor.objects.filter(id=actor.id).exists())
