from django.core.management.base import BaseCommand, CommandError
import fasttext


class Command(BaseCommand):
    help = 'build the model from the training data at ./export/train.txt'

    def handle(self, *args, **options):

        classifier = fasttext.supervised('export/train.txt', 'export/model', label_prefix='__label__', word_ngrams=1,
                                         bucket=2000000, thread=4)
        self.stdout.write(self.style.SUCCESS('Model is trained and ready at ./export/model'))

        self.stdout.write(self.style.SUCCESS('Done.'))
