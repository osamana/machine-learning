from django import forms
from . import models


class AddReviewForm(forms.Form):
    rating = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), label="Rating", required=True)
    members = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), label="No. of people", required=True)
    nights = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), label="Nights", required=True)
    review = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ), label="Review", required=True)
    hotel_id = forms.IntegerField(widget=forms.HiddenInput())


class PostAddFrom(forms.Form):
    likes = forms.IntegerField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ), label="Likes", required=True)
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ), label="Post text", required=True)


class TestTextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
        }
    ), label="Experimental text", required=True)


class SendMessageForm(forms.ModelForm):
    class Meta:
        model = models.HotelMessage
        fields = "__all__"
        widgets = {
            # 'hotel': forms.Select(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(SendMessageForm, self).__init__(*args, **kwargs)

        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'


class RegRequestForm(forms.ModelForm):
    class Meta:
        model = models.RegRequest
        fields = "__all__"
        widgets = {
            # 'hotel': forms.Select(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super(RegRequestForm, self).__init__(*args, **kwargs)

        for f in self.fields:
            self.fields[f].widget.attrs['class'] = 'form-control'
