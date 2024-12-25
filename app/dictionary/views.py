from django.shortcuts import render
from .models import Word


def index(request):
    return render(request, "pages/index.html")


def wordlist(request):
    wordList = Word.objects.all()

    content = {'wordList': wordList}
    for x in wordList:
        print(x)
    return render(request, "pages/wordlist.html", content)
