from rest_framework.test import APITestCase
from rest_framework import status
from django.core.urlresolvers import reverse
from .factories import UserFactory
import json

class AuthTests(APITestCase):

    def test_signup(self):
        """Ensure we can sign up a new user"""
        user = UserFactory.build()
        url = reverse("sign_up")
        data = {'username': user.username,
                'password': user.password}
        response = self.client.post(url, json.dumps(data), content_type='application/json')
        self.assertContains(response, 'client_id', status_code= status.HTTP_201_CREATED)
        self.assertContains(response, 'client_secret', status_code= status.HTTP_201_CREATED)

    def test_login(self):
        """Ensure we can login an existing user"""
        user = UserFactory.create()
        url = reverse("login")
        self.client.credentials(username=user.username, password=user.password)
        from nose.tools import set_trace; set_trace()
        response = self.client.get(url)
        self.assertContains(response, 'client_id', status_code= status.HTTP_200_OK)
        self.assertContains(response, 'client_secret', status_code= status.HTTP_200_OK)