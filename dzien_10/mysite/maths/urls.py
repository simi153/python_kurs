from django.contrib import admin
from django.urls import path, include

from maths.views import add, sub, div, mul, sqrt, pow_view, index, lista_elementow

urlpatterns = [
    path('', index),
    path('add/<a>/<b>', add),
    path('sub/<a>/<b>', sub),
    path('div/<a>/<b>', div),
    path('mul/<a>/<b>', mul),
    path('sqrt/<a>/<b>', sqrt),
    path('pow_view/<a>/<b>', pow_view),
    path('lista/',lista_elementow)
]
