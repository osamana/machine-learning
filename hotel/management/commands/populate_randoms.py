from django.core.management.base import BaseCommand
from hotel.models import Review
import random


class Command(BaseCommand):
    help = "loops all hotels and populates random data for nights and members, these data are not tied like in the relationship bet. reviews and ratings"

    def handle(self, *args, **options):
        reviews = Review.objects.all()
        self.stdout.write('Started')

        for review in reviews:
            nights = random.randint(1, 10)
            members = random.randint(1, 6)
            review.nights = nights
            review.members = members
            review.save()

        self.stdout.write(self.style.SUCCESS('Done.'))
