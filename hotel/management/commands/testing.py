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
        self.stdout.write(self.style.SUCCESS('Reading hotels data...'))

        df = pd.read_csv(options['file_name'], sep='\t', encoding='utf-16')
        df.review = df.review.apply(clean)
        df['label'] = '__label__' + df.rating.astype(str)

        # with open(options['file_name'], 'r', encoding='utf-16') as file:
        #     reader = csv.reader(file, delimiter='\t')
        #
        #     cnt = 0
        #     for line in reader:
        #         print(line)
        #         cnt += 1
        #         if cnt >= 10:
        #             break

        from sklearn.model_selection import StratifiedShuffleSplit
        spl = StratifiedShuffleSplit(n_splits=1, test_size=0.3, random_state=123)
        for tr_ix, te_ix in spl.split(df.review, df.label):
            break
        with open('data/hotel.train', 'w', encoding='utf-8') as f:
            for lbl, txt in df[['label', 'review']].iloc[tr_ix].values:
                print(lbl, txt, file=f)
        with open('data/hotel.test', 'w', encoding='utf-8') as f:
            for lbl, txt in df[['label', 'review']].iloc[te_ix].values:
                print(lbl, txt, file=f)

        self.stdout.write(self.style.SUCCESS('Created training and test data > hotel.train, hotel.test'))
        classifier = fasttext.supervised('data/hotel.train', 'data/model', label_prefix='__label__', word_ngrams=2,
                                         bucket=2000000, thread=4)
        self.stdout.write(self.style.SUCCESS('Model is trained and ready'))

        text = [u"لا احبه الغرف صغيرة", ]
        labels = classifier.predict_proba(text, k=3)
        print(labels)

        self.stdout.write(self.style.SUCCESS('Done.'))
