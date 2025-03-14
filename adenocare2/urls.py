from django.contrib import admin
from django.urls import path
from app1.views import index, symptom_checker, lung_analysis, community, home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('home/', home, name='home'),  # Corrected
    path('symptom_checker/', symptom_checker, name='symptom_checker'),  # Corrected
    path('lung_analysis/', lung_analysis, name='lung_analysis'),  # Corrected
    path('community/', community, name='community'),  # Corrected
]
