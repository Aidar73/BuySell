from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('BuySell')


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