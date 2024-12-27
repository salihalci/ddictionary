from django.urls import path

from . import views


urlpatterns = [
    path('', views.wordlist, name="word_list"),
    path('word_save', views.word_save, name="word_save"),
    path('word_search', views.word_search, name="word_search"),
    path('word_update/<str:pk>', views.word_update, name="word_update"),
    path('word_delete/<str:pk>', views.word_delete, name="word_delete"),
    path('success', views.success, name="success"),
    path('home', views.home, name="home"),
]
