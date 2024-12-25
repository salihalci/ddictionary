from django.shortcuts import render, redirect
from .models import Word
from .forms import WordSaveUpdate


def index(request):
    return render(request, "pages/index.html")


def wordlist(request):
    wordList = Word.objects.all()

    context = {'wordList': wordList}
    for x in wordList:
        print(x)
    return render(request, "pages/wordlist.html", context)


def word_save(request):

    print(request.method)

    if request.method == 'POST':
        form = WordSaveUpdate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:  # yeni form oluşturup boş bir form açıyor
        form = WordSaveUpdate()
        context = {'form': form}
        return render(request, "pages/word_save.html", context)


def success(request):
    return render(request, "pages/success.html")


def word_update(request, pk):
    print(pk)
    if request.method == 'GET':
        word = Word.objects.get(id=pk)

        form = WordSaveUpdate(instance=word)

        print("Update form loaded.")
        context = {'form': form}
        return render(request, 'pages/word_update.html', context)

    if request.method == 'POST':

        word = Word.objects.get(id=pk)
        print(word)
        form = WordSaveUpdate(request.POST, instance=word)

        if form.is_valid():

            form.save()
            print("Update executed.")

            return redirect('word_list')


def word_delete(request, pk):
    word = Word.objects.get(id=pk)
    context = {'word': word}
    return render(request, 'pages/word_delete.html', context)
