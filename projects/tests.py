from django.test import TestCase, client

from .models import Project
from members.models import User
from attachments.models import Attachment


client = client.Client()


class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin', faculty_number='7023')
        self.user.set_password('admin')
        self.user.save()

    def test_add_new_project(self):
        client.login(username='admin', password='admin')
        before_add = Project.objects.all().count()
        response = client.post('/projects/add/', {
            'team': [self.user.pk],
            'name': 'New project',
            'description': 'spam',
            'tasks': 'spam',
            'targets': 'spam',
            'target_group': 'spam',
            'schedule': 'spam',
            'resources': 'spam',
            'finance_description': 'spam'})
        after_add = Project.objects.all().count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(before_add + 1, after_add)

    def test_adding_new_project_from_user_who_is_not_logged(self):
        before_add = Project.objects.all().count()
        response = client.post('/projects/add/', {
            'team': [self.user.pk],
            'name': 'New project',
            'description': 'spam',
            'tasks': 'spam',
            'targets': 'spam',
            'target_group': 'spam',
            'schedule': 'spam',
            'resources': 'spam',
            'finance_description': 'spam'})
        after_add = Project.objects.all().count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(before_add, after_add)

    def test_adding_incomplete_project(self):
        client.login(username='admin', password='admin')
        before_add = Project.objects.all().count()
        response = client.post('/projects/add/', {
            'team': [self.user.pk],
            'name': 'New project',
            'description': 'spam',
            'target_group': 'spam',
            'schedule': 'spam',
            'resources': 'spam',
            'finance_description': 'spam'})
        after_add = Project.objects.all().count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(before_add, after_add)
