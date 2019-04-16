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

        groups = [1, 2, 3, 4, 5, 6]  # should get this dynamically and from data

        for index, hotel in enumerate(hotels):
            word_ocr_groups = {}
            for g in groups:
                word_ocr = {}
                for word in word_list:
                    word_counter = 0
                    for review in hotel.reviews.filter(members=g):
                        count = get_occurrences(word, review.review_text)
                        word_counter += count
                    word_ocr[word] = word_counter
                word_ocr_groups[g] = word_ocr
            hotel.word_ocr_groups = word_ocr_groups
            hotel.save()
            if index % 50 == 0:
                print("Processed hotels: {0}\r".format(index), end="")
        self.stdout.write(self.style.SUCCESS('Done.'))
