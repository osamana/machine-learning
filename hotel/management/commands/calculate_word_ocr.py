from django.core.management.base import BaseCommand
from hotel.models import Hotel
from django.db import models
import re


def get_occurrences(word, text):
    occ_list = [m.start() for m in re.finditer(word, text)]
    return len(occ_list)


class Command(BaseCommand):
    help = "loops all hotels and create the weighted data and caches those to the hotel's model'"

    def handle(self, *args, **options):
        hotels = Hotel.objects.all()
        self.stdout.write('Started')
        """
        what is needed:
        we need to get the occurrence of each word in the list of words above in
        each review for each hotel

        pseudo code:
        create a new field on Hotel > word_ocr (json)
        word_list = ['word1', 'word2' , ...etc]
        
        for hotel in hotels:
            word_ocr = {}
            for word in word_list:
                word_counter = 0
                for review in hotel.reviews:
                    count = get_occurrence(word, review.text)
                    word_counter += count
                word_ocr[word] = word_counter
            hotel.word_ocr = word_ocr
            hotel.save()
        """
        word_list = [
            u'خدم',
            u'انترنت',
            u'غرف',
        ]

        for hotel in hotels:
            word_ocr = {}
            for word in word_list:
                word_counter = 0
                for review in hotel.reviews.all():
                    count = get_occurrences(word, review.review_text)
                    word_counter += count
                word_ocr[word] = word_counter
            hotel.word_ocr = word_ocr
            hotel.save()

        self.stdout.write(self.style.SUCCESS('Done.'))
