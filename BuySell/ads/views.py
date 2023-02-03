from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ads.models import *


def index(request):
    ads_list = Ads.objects.order_by('-time_created').all()
    paginator = Paginator(ads_list, 10)
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