from django import forms

from ads.models import Ads, Photo


class AdsForm(forms.ModelForm):
    class Meta:
        model = Ads
        fields = ['sell_rent', 'city', 'category', 'title', 'text', 'price']


class AdsPhotoForm(AdsForm):
    images = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple': True}))

    class Meta(AdsForm.Meta):
        fields = AdsForm.Meta.fields + ['images',]

# class AdsForm(forms.Form):
#     name = forms.CharField(label=u'Локация')
#     photos = forms.ImageField(label=u'Фотографии', widget=forms.FileInput(attrs={'multiple': 'multiple'}))