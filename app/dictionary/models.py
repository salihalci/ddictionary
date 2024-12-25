from django.db import models

# Create your models here.


class Word(models.Model):
    word_en = models.CharField(max_length=64)
    translation_tr = models.CharField(max_length=256)

    def __str__(self):
        return self.word_en + "-"+self.translation_tr
