from rest_framework import serializers
from genres.models import Genre
from .models import Movie
from genres.serializers import GenreSerializer




class MovieSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=127)
    duration = serializers.CharField(max_length=10)
    premiere = serializers.DateField()
    classification = serializers.IntegerField()
    synopsis = serializers.CharField()

    genres =  GenreSerializer(many=True)
    

    def create(self, validated_data: dict) -> Movie:

        genre_data = validated_data.pop("genres")
        
        movie = Movie.objects.create(**validated_data)

        for genre in genre_data:
            genre_data = Genre.objects.get_or_create(**genre)[0]

            movie.genres.add(genre_data)
            
        return movie
    

    def update(self, instance, validated_data: dict) -> Movie:
        genre_data = validated_data.pop("genres")
        
        for key, value in validated_data.items():
            setattr(instance, key, value) 
            instance.save()
            instance.genres.clear()

            for genre in genre_data:
                genre = Genre.objects.get_or_create(**genre)[0]

                instance.genres.add(genre)

            return instance
        


