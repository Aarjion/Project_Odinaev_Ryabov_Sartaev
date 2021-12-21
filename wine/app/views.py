from django.shortcuts import render
from .models import Wine


def index(request):
    return render(request, 'index.html')


def result(request):
    if 'wine_data' in request.GET:
        wine_data = request.GET['wine_data']
        wine = Wine.create(wine_data['fixed_acidity'], wine_data['volatile_acidity'], wine_data['citric_acid'],
                           wine_data['residual_sugar'], wine_data['chlorides'], wine_data['free_sulfur'],
                           wine_data['total_sulfur'], wine_data['density'], wine_data['pH'], wine_data['sulphates'],
                           wine_data['alcohol'])
        wine.quality = wine.find_quality()
        return render(request, 'result.html', {'result': wine})
