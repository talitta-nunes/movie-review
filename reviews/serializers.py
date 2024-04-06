from rest_framework import serializers
from users.models import User

from .models import Review


class CriticSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "first_name", "last_name"]


class ReviewSerializer(serializers.ModelSerializer):

    critic = CriticSerializer(read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "stars",
            "review",
            "spoilers",
            "movie_id",
            "critic",
            "recomendation",
        ]
        extra_kwargs = {
            "recomendation": {
                "required": False,
            },
            "spoilers": {
                "required": False,
            },
        }

    read_only_fields = ["id", "critic", "movie_id"]
