from genres.models import Genre
from genres.serializers import GenreSerializer
from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField(allow_blank=True, allow_null=True)

    genres = GenreSerializer(many=True)

    def create(self, validated_data: dict) -> Movie:
        genres_list = validated_data.pop("genres")

        movie_obj = Movie.objects.create(**validated_data)

        for genres_dict in genres_list:
            genre_obj, _ = Genre.objects.get_or_create(**genres_dict)
            movie_obj.genres.add(genre_obj)

        return movie_obj

    def update(self, movie: Movie, validated_data: dict) -> Movie:
        genres_list = validated_data.pop("genres", None)
        if genres_list:
            genres_obj_list = []
            for genre_dict in genres_list:
                genre_obj, _ = Genre.objects.get_or_create(**genre_dict)
                genres_obj_list.append(genre_obj)

            movie.genres.set(genres_obj_list)
        for key, value in validated_data.items():
            setattr(movie, key, value)
        movie.save()

        return movie
