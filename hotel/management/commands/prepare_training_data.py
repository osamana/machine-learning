from django.core.management.base import BaseCommand, CommandError
from hotel.models import *
import re


def clean(s):
    s = re.sub(r"([.!?,'/()])", r" \1 ", s)
    s = re.sub(r"[اأإآءئ]", "ا", s)
    s = re.sub(r"[هة]", "ه", s)
    return s


class Command(BaseCommand):
    help = 'Prepares the reviews from database and reformat it for model building input'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Exporting data to ./export'))

        with open('export/train.txt', 'w', encoding='utf-8') as file:
            # reviews = Review.objects.all()[:100]
            reviews = Review.objects.all()
            for review in reviews:
                file.write(u'__label__{} {}\n'.format(review.rating, clean(review.review_text)))

        self.stdout.write(self.style.SUCCESS('Training file is ready /export/train.txt'))
        self.stdout.write(self.style.SUCCESS('Done.'))
