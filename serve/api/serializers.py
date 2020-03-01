from rest_framework import serializers

from serve.models import Movie

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = "Movie"
        model = Movie

        fields = ('__all__')

class MovieNameSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = "Movie"
        model = Movie

        fields = ('Id', 'Name')

class MovieYearSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = "Movie"
        model = Movie

        fields = ('YearNo', 'Name')

class MovieYearNoSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = "Movie"
        model = Movie

        fields = ('Name', 'YearNo')