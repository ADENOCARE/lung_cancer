from django.contrib import admin
from django.urls import path
from app1.views import index, auth, symptom_checker, lung_analysis, community

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('auth/', auth, name='auth'),  # Corrected
    path('symptom_checker/', symptom_checker, name='symptom_checker'),  # Corrected
    path('lung_analysis/', lung_analysis, name='lung_analysis'),  # Corrected
    path('community/', community, name='community'),  # Corrected
]
