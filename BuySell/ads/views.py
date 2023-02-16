from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect
from ads.forms import AdsForm, AdsPhotoForm, SearchForm
from ads.models import *


def index(request):
    ads_list = Ads.objects.filter(is_published=True).order_by('-time_created')
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
    if not ads.is_published and request.user != ads.seller:
        return redirect('ads_deactivated')
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
    if request.user == seller:
        ads_list = Ads.objects.filter(seller=seller.pk).order_by('-time_created')
    else:
        ads_list = Ads.objects.filter(is_published=True).filter(seller=seller.pk).order_by('-time_created')
    paginator = Paginator(ads_list, 10)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'profile.html', {
        'page': page,
        'paginator': paginator,
        'seller': seller,
    })


def ads_deactivated(request):
    return render(request, "ads_deactivated.html")


def page_not_found(request, exception):
    return render(request, "misc/ads_deactivated.html", {"path": request.path}, status=404)


def server_error(request):
    return render(request, "misc/500.html", status=500)


def catalog(request):
    category_list = SuperCategory.objects.all()
    return render(request, 'catalog.html', {'category_list': category_list})


def search(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        city = form.cleaned_data['city']
        if city:
            ads_list = Ads.objects.filter(city=city)
        else:
            ads_list = Ads.objects.filter(
                Q(title__iregex=query) |
                Q(text__iregex=query) |
                Q(category__title__iregex=query) |
                Q(category__supercategory__title__iregex=query)
            ).order_by('-time_created')
    else:
        ads_list = Ads.objects.all().order_by('-time_created')
    paginator = Paginator(ads_list, 20)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return render(request, 'search.html', {
        'form': form,
        'page': page,
        'paginator': paginator
    })