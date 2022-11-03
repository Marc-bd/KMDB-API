from rest_framework import serializers
from .models import Review




class ReviewSerializer(serializers.ModelSerializer):

    critic = serializers.SerializerMethodField()

    stars = serializers.DecimalField(max_digits=10, decimal_places=0, max_value=10)


    def get_critic(self, instance):
        return {
            "id": instance.user.id,
            "first_name": instance.user.first_name,
            "last_name": instance.user.last_name
        }

    class Meta:
        model = Review
        fields = ["id", "stars", "review", "spoilers", "recomendation", "movie_id", "critic"]
       