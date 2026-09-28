from rest_framework import serializers
from movies.models import Movie
from genres.models import Genre
from actors.models import Actor

class MovieSerializer(serializers.Serializer):
    title = serializers.CharField()
    genre = serializers.PrimaryKeyRelatedField(
        queryset = Genre.objects.all(),
    )
    release_date = serializers.DateField()
    actors = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(),
        many=True,
    )
    resume = serializers.CharField()


class MovieModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    def validate_release_date(self, value):
        print(f"DEBUG: validate_release_date chamado com value={value}")  # ← AQUI
        if value.year < 1990:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior a 1990')
        return value
    