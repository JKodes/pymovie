from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context ={
        'movies' : ['titanic', 'maximum overdrive', 'its a mad mad world']
    }
    return render(request, 'movies/index.html', { context })

def about(request):
    return render(request, 'movies/about.html', {})