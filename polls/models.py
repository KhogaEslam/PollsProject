from __future__ import unicode_literals
from datetime import date

from django.db import models

# Create your models here.

class Question(models.Model):
    qText = models.CharField(max_length = 200)
    pubDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.qText

    def isPublishedBeforeToday(self):
        return date.today() > self.pubDate.date()

    isPublishedBeforeToday.short_description = 'Puplished Before Today ?'
    isPublishedBeforeToday.boolean = True

class Choice(models.Model):
    cText = models.CharField(max_length = 50)
    vNum = models.IntegerField()
    pQuest = models.ForeignKey(Question)

    def __str__(self):
        return self.cText
