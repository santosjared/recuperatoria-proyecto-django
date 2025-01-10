from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MedicamentViewSet, ClientViewSet, search_medicament

router = DefaultRouter()
router.register('medicaments', MedicamentViewSet)
router.register('clients', ClientViewSet)

urlpatterns = router.urls + [
    path('medicaments/search/', search_medicament, name='search-medicament'),
]
