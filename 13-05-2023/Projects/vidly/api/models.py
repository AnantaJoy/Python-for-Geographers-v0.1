from django.db import models
from tastypie.resources import ModelResource
from movies.models import Movie

# Create your models here.
class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        allowed_methods = ['get']
        filtering = {
            'title': ['exact', 'startswith'],
            'release_year': ['exact', 'lt', 'lte', 'gte', 'gt'],
        }
        ordering = ['title', 'release_year']
        excludes = ['id']
        include_resource_uri = False
        always_return_data = True
        limit = 0
        max_limit = 0
    