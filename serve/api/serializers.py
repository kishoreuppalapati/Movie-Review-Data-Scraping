from rest_framework import serializers

from serve.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = "Movie"
        model = Movie

        fields = ('__all__')