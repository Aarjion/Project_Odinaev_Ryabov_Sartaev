import json

from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from .models import Wine


def index(request):
    return render(request, 'index.html')


def result(request):
    wine = Wine.create(request.GET['fixed_acidity'], request.GET['volatile_acidity'], request.GET['citric_acid'],
                       request.GET['residual_sugar'], request.GET['chlorides'], request.GET['free_sulfur'],
                       request.GET['total_sulfur'], request.GET['density'], request.GET['pH'], request.GET['sulphates'],
                       request.GET['alcohol'])
    wine.quality = wine.find_quality()
    #govnokod2
    cock = {'fixed_acidity': request.GET['fixed_acidity'], 'volatile_acidity': request.GET['volatile_acidity'], 'citric_acid': request.GET['citric_acid'],
                       'residual_sugar': request.GET['residual_sugar'], 'chlorides': request.GET['chlorides'], 'free_sulfur': request.GET['free_sulfur'],
                       'total_sulfur': request.GET['total_sulfur'], 'density': request.GET['density'], 'pH': request.GET['pH'], 'sulphates': request.GET['sulphates'],
                       'alcohol': request.GET['alcohol']}
    return render(request, 'result.html', {'result': wine, 'cock': json.dumps(cock)})