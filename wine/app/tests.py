from django.test import TestCase
from .models import Wine


def test():
    wine = Wine.create(7, 0.27, 0.36, 20.7, 0.045, 45, 170, 1.001, 3, 0.45, 8.8)
    return wine.find_quality()


print(test())
