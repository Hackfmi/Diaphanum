# -*- encoding:utf-8 -*-
from django.test import TestCase, client

from .models import User
from projects.models import Project

from casper.tests import CasperTestCase
import os.path

class TestLogin(CasperTestCase):
    def test_login_form(self):
        self.assertTrue(self.casper(os.path.join(os.path.dirname(__file__), 'casper-tests/testLoginForm.js')))
        
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

        self.project = Project.objects.create(
            user=kril,
            flp=kril,
            name='New project',
            description='spam',
            tasks='spam',
            targets='spam',
            target_group='spam',
            schedule='spam',
            resources='spam',
            finance_description='spam'
            )

    def test_search_users_in_en(self):
        response = client.get('/members/search/i/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content)

    def test_search_users_in_bg(self):
        response = client.get('/members/search/{}/'.format(self.gogo.first_name))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.content)

    def test_user_not_found(self):
        response = client.get('/members/search/pe/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, '[]')

    def test_get_user_projects(self):
        client.login(username='Kril', password='kril')
        response = client.get('/members/profile/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['projects']), 1)
        self.assertEqual(response.context['projects'][0].pk, self.project.pk)