from django.http import JsonResponse
from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie, Actor


def main(request):
    return redirect('home')


from django.core.paginator import Paginator

def home(request):
    actor_id = request.GET.get('actor_id')
    content_type = request.GET.get('type', 'all')
    year = request.GET.get('year', '')
    
    search = request.GET.get('search', '')
    if request.method == "POST":
        search = request.POST.get('search', '')

    movies = Movie.objects.all().order_by('-date')

    if search:
        movies = movies.filter(title__icontains=search)
    if actor_id:
        movies = movies.filter(actor__id=actor_id)
    if content_type in ['film', 'tv_show']:
        movies = movies.filter(content_type=content_type)
    if year and year.isdigit():
        movies = movies.filter(year=year)

    count = movies.count()

    paginator = Paginator(movies, 80)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'search': search,
        'movies': page_obj,
        'count': count,
        'current_type': content_type,
        'current_year': year,
        'actor_id': actor_id,
        'page_obj': page_obj,
    }

    return render(request, 'home.html', context)


def movie_view(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movies')
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {'form': form})


def actor_autocomplete(request):
    query = request.GET.get('term', '')
    actors = Actor.objects.filter(name__icontains=query)[:10]
    results = [{'id': actor.id, 'label': actor.name} for actor in actors]
    return JsonResponse(results, safe=False)
