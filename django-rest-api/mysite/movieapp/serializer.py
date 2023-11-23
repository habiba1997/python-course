from .models import Movie
from rest_framework import serializers


class MovieSerializer(serializers.ModelSerializer):
    # meta means that it need info about itself an dhere it neeed model that it will serialize
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Movie
        fields = ('name', 'description', 'rating', 'image')
