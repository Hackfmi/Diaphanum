from datetime import time

from django.test import client, TestCase
from members.models import Member
from .models import Protocol, Topic

client = client.Client()

class ProtocolTest(TestCase):
    def setUp(self):
        self.kril = Member.objects.create(
            username='Kril',
            faculty_number='61277',
            email='kril@gmail.com',)
        self.kril.set_password('kril')
        self.kril.save()

        self.topic1 = Topic.objects.create(name='1', description='first')
        self.topic2 = Topic.objects.create(name='2', description='second')
        self.topic3 = Topic.objects.create(name='3', description='third')

    def test_add_protocol(self):
        client.login(username='Kril', password='kril')
        response = client.post('/protocols/add/', {
                        "number": "13/11/1992/1234",
                        "scheduled_time": time(9, 0, 0),
                        "start_time": time(10, 0, 0),
                        "quorum": 32,
                        "absent": 8,
                        "attendents": self.kril.pk,
                        "topics": [self.topic1.pk, self.topic2.pk, self.topic3.pk],
                        "voted_for": 4,
                        "voted_against": 16,
                        "voted_abstain": 12,
                        "information": 'this is the best protocol ever',})

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(Protocol.objects.all()))

    def test_update_user_information(self):
        client.login(username='Kril', password='kril')
        response = client.post('/protocols/add/', {
                        "number": "13/11/1992/1234",
                        "scheduled_time": time(9, 0, 0),
                        "start_time": time(10, 0, 0),
                        "quorum": 32,
                        "absent": 8,
                        "attendents": self.kril.pk,
                        "topics": [self.topic1.pk, self.topic2.pk, self.topic3.pk],
                        "voted_for": 4,
                        "voted_against": 16,
                        "voted_abstain": 12,
                        "information": 'this is the best protocol ever',})

        self.assertEqual(1, len(self.kril.attended_meetings()))


