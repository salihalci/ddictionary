from django.urls import path

from . import views


urlpatterns = [
    path('', views.wordlist),
    path('word_save', views.word_save, name="word_save"),
    path('success', views.success, name="success"),
]
