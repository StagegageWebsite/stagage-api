from rest_framework.test import APITestCase
from rest_framework import status
from .factories import UserFactory


class TestAPI(APITestCase):

    def setUp(self):
        self.password = "admin"
        self.user = UserFactory(password=self.password)


    def test_login(self):
        data = {'username': self.user.username,
                'password': self.password}
        response = self.client.post('/auth/login/', data)
        from nose.tools import set_trace; set_trace()
        self.assertContains(response, 'key', status_code=status.HTTP_200_OK)


