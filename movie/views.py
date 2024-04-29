from django.shortcuts import render
from .models import Movies
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    movies = Movies.objects.all()
    # This block of code is for searching
    movie_name = request.GET.get('search')
    if movie_name != '' and movie_name is not None:
        movies = Movies.objects.filter(name__icontains = movie_name)
    # End of Searching code

    # This block is for pagination
    paginator = Paginator(movies,2)
    page = request.GET.get('page')
    movies = paginator.get_page(page)
    # End of pagination code

    return render(request,'index.html',{'movies':movies})
