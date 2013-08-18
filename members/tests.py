# -*- encoding:utf-8 -*-
from django.test import TestCase, client

from .models import User

client = client.Client()


class TestUserSearch(TestCase):
    def setUp(self):
        kril = User.objects.create(
            username='Kril',
            first_name='Kril',
            faculty_number='61277',
            email='kril@gmail.com',)
        kril.set_password('kril')
        kril.save()

        ivo = User.objects.create(
            username='ivo',
            first_name='Ivailo',
            faculty_number='61279',
            email='ivo@gmail.com',)
        ivo.set_password('root')
        ivo.save()

        self.gogo = User.objects.create(
            username='gogo',
            first_name='Георги',
            faculty_number='63279',
            email='gogo@gmail.com',)
        self.gogo.set_password('admin')
        self.gogo.save()

    def test_search_users_in_en(self):
        response = client.get('/search/i/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content)

    def test_search_users_in_bg(self):
        response = client.get('/search/{}/'.format(self.gogo.first_name))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content)

    def test_user_not_found(self):
        response = client.get('/search/pe/')
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.content)


