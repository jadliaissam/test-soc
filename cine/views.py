from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from cine.models import Movie, Actor, Review
from cine.serializers import MovieSerializer, ReviewSerializer, ActorSerializer


# Create your views here.

class MovieViewSet(ModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

    # To respect restfull, we should use POST to create a review and GET to get all reviews of a movie.
    @action(detail=True, methods=['POST', 'GET'], url_path='reviews', serializer_class=ReviewSerializer)
    def handle_reviews(self, request, pk):
        if request.method == 'GET':
            movie = self.get_object()
            reviews = movie.reviews.all()
            return Response({
                'status': status.HTTP_200_OK,
                'data': ReviewSerializer(reviews, many=True).data
            })
        else:
            serializer = ReviewSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            review = serializer.save()
            return Response({
                'status': status.HTTP_201_CREATED,
                'data': ReviewSerializer(review).data
            })


class ActorViewSet(ModelViewSet):
    serializer_class = ActorSerializer
    queryset = Actor.objects.all()


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()
