from django.shortcuts import render, redirect
from .models import Word
from .forms import WordSave


def index(request):
    return render(request, "pages/index.html")


def wordlist(request):
    wordList = Word.objects.all()

    content = {'wordList': wordList}
    for x in wordList:
        print(x)
    return render(request, "pages/wordlist.html", content)


def word_save(request):

    print(request.method)

    if request.method == 'POST':
        form = WordSave(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:  # yeni form oluşturup boş bir form açıyor
        form = WordSave()
        context = {'form': form}
        return render(request, "pages/word_save.html", context)


def success(request):
    return render(request, "pages/success.html")
