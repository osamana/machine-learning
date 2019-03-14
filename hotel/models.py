from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Hotel(models.Model):
    """Declaration of the Hotel object."""

    name = models.CharField(max_length=255)

    def __repr__(self):
        return f'<Hotel: {self.name}>'

    def __str__(self):
        return f'{self.name}'

    def reviews_count(self):
        return self.reviews.count()

    def get_absolute_url(self):
        return reverse('hotel-detail', kwargs={
            'pk': self.pk,
        })


class Review(models.Model):
    rating = models.SmallIntegerField(verbose_name="Rating", blank=False, null=False)
    review_text = models.TextField(verbose_name="Review text", blank=False)
    hotel = models.ForeignKey(Hotel, related_name='reviews', on_delete=models.CASCADE)

    def __repr__(self):
        return f'<Review: {self.rating}>'

    def __str__(self):
        return f'{self.rating}'

    # for prototyping only
    def get_ratings_range(self):
        return range(1, self.rating)


class Post(models.Model):
    text = models.TextField(verbose_name="Post text")
    likes = models.IntegerField(verbose_name="Likes", default=0)

    def __repr__(self):
        return f'<Post: {self.text}>'

    def __str__(self):
        return f'{self.text}'
