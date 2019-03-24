from django import forms


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
