
from django.contrib import admin
from django.urls import path
from genres.views import genre_view

def hello_view(request):    
    return JsonResponse({'id': 1, 'name': "Titanic", 'year': 1997, 'rating': 7.8})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', genre_view, name='genre-list')
]
