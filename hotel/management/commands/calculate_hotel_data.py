from django.core.management.base import BaseCommand
from hotel.models import Hotel


class Command(BaseCommand):
    help = "loops all hotels and create the weighted data and caches those to the hotel's model'"

    def handle(self, *args, **options):
        hotels = Hotel.objects.all()
        self.stdout.write('Started')

        for hotel in hotels:
            hotel.calculate_average_rating()  # average rating (weighted)
            hotel.calculate_residences()  # total members who stayed on that hotel for a time
            hotel.calculate_nights()  # total number of nights stayed on that hotel by all members
            hotel.calculate_average_members_per_stay()  # average member count per stay (a review record is a stay)
            hotel.calculate_average_nights_per_stay()  # average nights count per stay (a review record is a stay)
            hotel.plot_membercount_avgrating()

            hotel.save()  # must save (above methods don't commit to database)

        self.stdout.write(self.style.SUCCESS('Done.'))
