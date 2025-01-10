from django.test import TestCase
from rest_framework import status
from .models import Medicament

class TestCategories(TestCase):
    def setUp(self):
        Medicament.objects.create(
            name='Asperina',
            price='5.00',
            stock=200,
            description='esto pertenece a la categoria de Analgesico',
            expire_date="2025-01-01"
            )
    
    def test_search_medicament(self):
        response = self.client.get('/medicaments/search/', {'name': 'Aspirina'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], "Aspirina")

    def test_client_list(self):
        response = self.client.get('/clients')
        self.assertContains(response, status.HTTP_200_OK, html=True)
# Create your tests here.
