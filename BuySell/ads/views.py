from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from ads.forms import AdsForm, AdsPhotoForm
from ads.models import *


def index(request):
    ads_list = Ads.objects.order_by('-time_created').all()
    paginator = Paginator(ads_list, 20)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'index.html', {
        'title': 'BuySell: недвижимость, транспорт, вещи',
        'page': page,
        'paginator': paginator
    })


def ads_view(request, city_slug, cat_slug, ads_id):
    ads = get_object_or_404(Ads, pk=ads_id)
    return render(request, 'ads_view.html', {
            'ads': ads,
    })


@login_required
def ads_new(request):
    if request.method == 'POST':
        form = AdsPhotoForm(request.POST or None, request.FILES or None)
        files = request.FILES.getlist('images')
        if form.is_valid():
            ads = form.save(commit=False)
            ads.seller = request.user
            ads.save()
            for f in files:
                Photo.objects.create(ads=ads, image=f)
            return redirect('ads_view', city_slug=ads.city.city_slug, cat_slug=ads.category.cat_slug, ads_id=ads.pk)
        return render(request, "new_post.html", {"form": form})
    form = AdsPhotoForm()
    return render(request, "ads_new_edit.html", {"form": form})


@login_required
def ads_edit(request, city_slug, cat_slug, ads_id):
    ads = get_object_or_404(Ads, pk=ads_id)
    if request.method == 'GET':
        if request.user != ads.seller:
            return redirect('ads_view', city_slug=ads.city.city_slug, cat_slug=ads.category.cat_slug, ads_id=ads.pk)
    form = AdsPhotoForm(request.POST or None, request.FILES or None, instance=ads)
    if request.method == 'POST':
        files = request.FILES.getlist('images')
        if form.is_valid():
            form.save()
            Photo.objects.filter(ads=ads).delete()
            for f in files:
                Photo.objects.create(ads=ads, image=f)
            return redirect('ads_view', city_slug=ads.city.city_slug, cat_slug=ads.category.cat_slug, ads_id=ads.pk)
    return render(request, 'ads_new_edit.html', {'form': form, 'ads': ads})


@login_required
def ads_delete(request, city_slug, cat_slug, ads_id):
    ads = get_object_or_404(Ads, pk=ads_id)
    if request.user != ads.seller or request.method != 'GET':
        return redirect('ads_view', city_slug=ads.city.city_slug, cat_slug=ads.category.cat_slug, ads_id=ads.pk)
    ads.delete()
    return redirect('index')


def profile(request, username):
    seller = get_object_or_404(User, username=username)
    ads_list = Ads.objects.filter(seller=seller.pk)
    paginator = Paginator(ads_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'profile.html', {
        'page': page,
        'paginator': paginator,
        'seller': seller,
    })


# views for image
# def add_location(request):
#     if request.method == 'GET':
#         form = LocationForm()
#         return render(request, 'add_location.html', {'form': form})
#     elif request.method == 'POST':
#         form = LocationForm(request.POST, requst.FILES)
#         if form.is_valid():
#             location = Location.objects.create(user=request.user, name=form.cleaned_data['name'])
#             for f in request.FILES.getlist('photos'):
#                 data = f.read() #Если файл целиком умещается в памяти
#                 photo = Photo(location=location)
#                 photo.image.save(f.name, ContentFile(data))
#                 photo.save()
#                 return redirect(location) #Надо определить get_absolute_url() в модели
#         else:
#             return render(request, 'add_location.html', {'form': form})