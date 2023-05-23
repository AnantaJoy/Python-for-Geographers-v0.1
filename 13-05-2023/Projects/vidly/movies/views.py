from django.shortcuts import render, get_object_or_404  
from django.http import HttpResponse, Http404
from .models import Genre, Movie

# Create your views here.
def index(request):
    movies = Movie.objects.all()
    # output = ','.join([movie.title for movie in Movie.objects.all()])
    # Movie.objects.filter()
    # Movie.objects.get(1)
    # return HttpResponse(output)
    # return render(request, 'movies/index.html')
    return render(request, 'movies/index.html', {'movies': movies})

def detail(request, movie_id):
    # return HttpResponse(movie_id)
    
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})
   