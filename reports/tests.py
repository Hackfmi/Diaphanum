from django.test import client, TestCase
from members.models import User
from .models import Report
from protocols.models import Topic


client = client.Client()


class ReportTest(TestCase):
    def setUp(self):
        self.kril = User.objects.create(
            username='Kril',
            faculty_number='61277',
            email='kril@gmail.com',)
        self.kril.set_password('kril')
        self.kril.save()

        self.topic1 = Topic.objects.create(
            name='1',
            description='first',
            voted_for=13,
            voted_against=4,
            voted_abstain=5)
        self.topic2 = Topic.objects.create(
            name='2',
            description='second',
            voted_for=13,
            voted_against=4,
            voted_abstain=5)
        self.topic3 = Topic.objects.create(
            name='3',
            description='third',
            voted_for=13,
            voted_against=4,
            voted_abstain=5)


    def test_add_report(self):
        client.login(username='Kril', password='kril')
        response = client.post('/reports/add/', {
                        "addressed_to": "Hackfmi",
                        "reported_from": self.kril.pk,
                        "content": "This is a report test",
                        "copies": [self.topic1.pk, self.topic2.pk, self.topic3.pk],
                        "signed_from": "rozovo zaiche",})

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(Report.objects.all()))
