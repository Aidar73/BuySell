from django import forms

from ads.models import Ads, Photo, City


class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ['sell_rent', 'city', 'category', 'title', 'text', 'price']


class AdsPhotoForm(AdsForm):
    images = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(AdsForm.Meta):
        fields = AdsForm.Meta.fields + ['images',]


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
    city = forms.ModelChoiceField(queryset=City.objects.all(), required=False)

# class AdsForm(forms.Form):
#     name = forms.CharField(label=u'Локация')
#     photos = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))