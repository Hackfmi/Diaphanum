from django.test import TestCase, client

from .models import Project
from members.models import Member
from attachments.models import Attachment


client = client.Client()


class ProjectTest(TestCase):
    def setUp(self):
        self.user = Member.objects.create(username='admin', faculty_number='7023')
        self.user.set_password('admin')
        self.user.save()

    def test_add_new_project(self):
        client.login(username='admin', password='admin')
        before_add = Project.objects.all().count()
        response = client.post('/projects/add/',
                                 {'team': [self.user.pk],
                                  'name': 'New project',
                                  'description': 'spam',
                                  'tasks': 'spam',
                                  'targets': 'spam',
                                  'target_group': 'spam',
                                  'schedule': 'spam',
                                  'resources': 'spam',
                                  'finance_description': 'spam'})
        after_add = Project.objects.all().count()
        # import ipdb; ipdb.set_trace()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(before_add + 1, after_add)

