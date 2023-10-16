from django.db import models
from rest_framework import serializers

from cine.models import Movie, Review, Actor


class MovieSerializer(serializers.ModelSerializer):
    note = serializers.SerializerMethodField(method_name='average_note')

    def average_note(self, obj):
        movie_avg = obj.reviews.aggregate(models.Avg('grade')).get('grade__avg', 0)
        return movie_avg

    class Meta:
        model = Movie
        fields = '__all__'


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    grade = serializers.IntegerField(required=True)

    class Meta:
        fields = '__all__'
        model = Review

    def validate_grade(self, value):
        if value > 5 or value < 0:
            raise serializers.ValidationError('Grade must be between 0 and 5')
        return value

    def create(self, validated_data):
        return Review.objects.create(
            grade=validated_data.get('grade'),
            movie=validated_data.get('movie'),
        )
