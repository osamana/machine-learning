from django.shortcuts import render
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView, FormView, TemplateView
from .models import Hotel, Review, Post
from .forms import AddReviewForm, PostAddFrom, TestTextForm
from django.shortcuts import redirect
import fasttext
from django.conf import settings
import os
from django.urls import reverse



# Create your views here.
class HotelListView(ListView):
    http_method_names = [u'get']
    template_name = "hotels/list/hotel.html"
    context_object_name = "hotels"
    allow_empty = False
    paginate_by = 50
    model = Hotel


class HotelDetailView(DetailView):
    http_method_names = [u'get']
    template_name = "hotels/detail/hotel.html"
    context_object_name = "hotel"
    model = Hotel

    def get_context_data(self, **kwargs):
        context = super(HotelDetailView, self).get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.order_by("-id")
        hotel_id = self.object.id
        context['add_review_form'] = AddReviewForm(initial={"hotel_id": hotel_id})
        return context


class AdministrationView(TemplateView):
    http_method_names = [u'get']
    template_name = "hotels/admin.html"

    def get_context_data(self, **kwargs):
        context = super(AdministrationView, self).get_context_data(**kwargs)
        context['hotels_count'] = Hotel.objects.count()
        context['reviews_count'] = Review.objects.count()
        context['test_text_form'] = TestTextForm()
        return context


def add_review(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddReviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            target_hotel_id = int(form.cleaned_data['hotel_id'])
            target_hotel = Hotel.objects.get(id=target_hotel_id)

            Review.objects.create(
                hotel=target_hotel,
                rating=form.cleaned_data["rating"],
                review_text=form.cleaned_data["review"]
            )

            # redirect to a new URL:
            return redirect(target_hotel)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddReviewForm()

    return redirect("hotel-list")


class PostListView(ListView):
    http_method_names = [u'get']
    template_name = "hotels/list/post.html"
    context_object_name = "posts"
    allow_empty = True
    paginate_by = 50
    model = Post

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['post_add_form'] = PostAddFrom()
        return context


def add_post(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PostAddFrom(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            Post.objects.create(
                likes=form.cleaned_data["likes"],
                text=form.cleaned_data["text"]
            )

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PostAddFrom()

    return redirect("post-list")


def test_text(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TestTextForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            text = form.cleaned_data["text"]

            model_location = os.path.join(settings.BASE_DIR, 'export', 'model.bin')

            # load pertained model
            classifier = fasttext.load_model(model_location, label_prefix='__label__')

            # get the two best predictions

            test_case = [text, ]
            predictions = classifier.predict_proba(test_case, k=3)

            context = {
                'p_list': predictions[0],
                'text': text,
            }
            return render(request, 'hotels/predictions_results.html', context)




    # if a GET (or any other method) we'll create a blank form
    else:
        form = TestTextForm()

    return redirect("admin-portal")
