from django.db import models


class Wine(models.Model):
    fixed_acidity = models.FloatField('fixed acidity')
    volatile_acidity = models.FloatField('volatile acidity')
    citric_acid = models.FloatField('citric acid')
    residual_sugar = models.FloatField('residual sugar')
    chlorides = models.FloatField('chlorides')
    free_sulfur = models.FloatField('free sulfur')
    total_sulfur = models.FloatField('total sulfur')
    density = models.FloatField('density')
    pH = models.FloatField('pH')
    sulphates = models.FloatField('sulphates')
    alcohol = models.FloatField('alcohol')
    quality = models.FloatField('quality')
