from django.core.management.base import BaseCommand
from hotel.models import Hotel
from django.db import models


class Command(BaseCommand):
    help = "loops all hotels and create the weighted data and caches those to the hotel's model'"

    def handle(self, *args, **options):
        hotels = Hotel.objects.all()
        self.stdout.write('Started')

        # prune terminal hotels
        target1 = Hotel.objects.order_by('nights')[50:].values_list('pk', flat=True)
        target2 = Hotel.objects.order_by('-nights')[50:].values_list('pk', flat=True)
        target3 = Hotel.objects.order_by('residences')[50:].values_list('pk', flat=True)
        target4 = Hotel.objects.order_by('-residences')[50:].values_list('pk', flat=True)

        query1 = Hotel.objects.filter(pk__in=target1)
        query2 = Hotel.objects.filter(pk__in=target2)
        query3 = Hotel.objects.filter(pk__in=target3)
        query4 = Hotel.objects.filter(pk__in=target4)

        # find the intersection
        query = query1.intersection(query2, query3, query4)

        data = {
            'max_hotel_nights': query.order_by('-nights').first().nights,
            'min_hotel_nights': query.order_by('nights').first().nights,
            'max_hotel_residences': query.order_by('-residences').first().residences,
            'min_hotel_residences': query.order_by('residences').first().residences,
        }

        # data = {
        #     'max_hotel_nights': (query.aggregate(models.Max('nights')))['nights__max'],
        #     'min_hotel_nights': query.aggregate(models.Min('nights'))['nights__min'],
        #     'max_hotel_residences': query.aggregate(models.Max('residences'))['residences__max'],
        #     'min_hotel_residences': query.aggregate(models.Min('residences'))['residences__min'],
        # }
        print(data)

        for hotel in hotels:
            # hotel.calculate_average_rating()  # average rating (weighted)
            # hotel.calculate_residences()  # total members who stayed on that hotel for a time
            # hotel.calculate_nights()  # total number of nights stayed on that hotel by all members
            # hotel.calculate_average_members_per_stay()  # average member count per stay (a review record is a stay)
            # hotel.calculate_average_nights_per_stay()  # average nights count per stay (a review record is a stay)
            #
            # hotel.plot_membercount_avgrating()
            #
            # hotel.save()  # must save (above methods don't commit to database)

            hotel.calculate_rating_accuracy(data)
            hotel.save()

        self.stdout.write(self.style.SUCCESS('Done.'))
