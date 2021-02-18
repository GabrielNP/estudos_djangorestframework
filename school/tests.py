import json

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase, APIClient, RequestsClient
from requests.auth import HTTPBasicAuth

from school import models, serializer

# token = Token.objects.get(user__username='gabrielnp')
# client = APIClient()
# client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

class vaitomarnocu(APITestCase):
    client = APIClient()
    client.login(username='gabrielnp', password='123456')
    user = User.objects.get(username='gabrielnp')
    client.force_authenticate(user=user)

    def test_students(self):
        response = self.client.get('/students/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)