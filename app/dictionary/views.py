from django.shortcuts import render, redirect
from .models import Word
from .forms import WordSaveUpdate
import random


def index(request):
    return render(request, "pages/index.html")


def wordlist(request):
    wordList = Word.objects.all()

    context = {'wordList': wordList}

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


def home(request):
    return render(request, "pages/index.html")


def word_search(request):

    context = {}

    if request.method == "POST":
        print(request.POST.get("search_word"))
        wordList = Word.objects.filter(
            word_en__contains=request.POST.get("search_word"))

        if wordList.exists():  # TR kolonlarda kayıt bulunduysa
            print("TR record found!")
        else:  # EN searchte kayıt ara
            wordList = Word.objects.filter(
                translation_tr__contains=request.POST.get("search_word"))
            print("EN record found!")

        context = {'wordList': wordList}

    return render(request, "pages/wordlist.html", context)


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
    if request.method == 'GET':
        word = Word.objects.get(id=pk)
        context = {'word': word}
        return render(request, 'pages/word_delete.html', context)

    if request.method == 'POST':
        word = Word.objects.get(id=pk)
        word.delete()
        return redirect('word_list')


def remember_game(request):

    # I will change this 5 records to random
    allItems = list(Word.objects.all())
    wordList = random.sample(allItems, 5)

    context = {'wordList': wordList}

    return render(request, "pages/remembergame.html", context)
