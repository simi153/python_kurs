from django.contrib import admin
from django.urls import path, include

from polls.views import hello_view

urlpatterns = [
    path('', hello_view),
    path('<name>', hello_view),
]
