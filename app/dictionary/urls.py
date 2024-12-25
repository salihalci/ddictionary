from django.urls import path

from . import views


urlpatterns = [
    path('', views.wordlist, name="word_list"),
    path('word_save', views.word_save, name="word_save"),
    path('word_update/<str:pk>', views.word_update, name="word_update"),
    path('success', views.success, name="success"),
]
