from django.core.management.base import BaseCommand, CommandError
from hotel.models import *
import csv
import pandas as pd
import re
import fasttext


def clean(s):
    s = re.sub(r"([.!?,'/()])", r" \1 ", s)
    s = re.sub(r"[اأإآءئ]", "ا", s)
    s = re.sub(r"[هة]", "ه", s)
    return s


class Command(BaseCommand):
    help = 'import data from hotels sample data'

    def add_arguments(self, parser):
        parser.add_argument('file_name', type=str)

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Reading file: ' + options['file_name']))

        df = pd.read_csv(options['file_name'], sep='\t', encoding='utf-16')
        df.review = df.review.apply(clean)

        for index, row in df.iterrows():
            hotel_name = row['Hotel name']
            review = row['review']
            rating = row['rating']

            H = None
            Ra = None
            Re = None

            check = Hotel.objects.filter(name=hotel_name)
            if check.exists():
                H = check.first()
            else:
                # saves automatically
                H = Hotel.objects.create(
                    name=hotel_name
                )

            # create a new review object each time, since each row is a unique review
            # saves the object automatically
            Review.objects.create(
                rating=rating,
                review_text=review,
                hotel=H
            )

        self.stdout.write(self.style.SUCCESS('Done.'))
