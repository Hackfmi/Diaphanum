from datetime import time
from django.test import client, TestCase


from members.models import User
from .models import Protocol, Topic, Institution
from django.contrib.auth.models import Permission


client = client.Client()


class ProtocolTest(TestCase):
    def setUp(self):
        self.kril = User.objects.create(
            username='Kril',
            faculty_number='61277',
            email='kril@gmail.com',)
        self.kril.set_password('kril')
        self.kril.save()
        # self.kril.has_module_perms('protocols.add_protocol')
        self.kril.user_permissions.add(43)

        self.fake_kril = User.objects.create(
            username='FakeKril',
            faculty_number='80460',
            email='kril@kril.kril',)
        self.kril.set_password('FakeKril')
        self.fake_kril.save()

        # self.topic1 = Topic.objects.create(
        #     name='1',
        #     description='first',
        #     voted_for=13,
        #     voted_against=4,
        #     voted_abstain=5,
        #     protocol=self.protocol)
        # self.topic2 = Topic.objects.create(
        #     name='2',
        #     description='second',
        #     voted_for=13,
        #     voted_against=4,
        #     voted_abstain=5,
        #     protocol=self.protocol)
        # self.topic3 = Topic.objects.create(
        #     name='3',
        #     description='third',
        #     voted_for=13,
        #     voted_against=4,
        #     voted_abstain=5,
        #     protocol=self.protocol)

        self.institution = Institution.objects.create(name='SS')

    def test_add_protocol(self):
        client.login(username='Kril', password='kril')
        response = client.post('/protocols/add/', {
            "form-TOTAL_FORMS": 2,
            "form-INITIAL_FORMS": 0,
            "form-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "scheduled_time": time(9, 0, 0),
            "start_time": time(10, 0, 0),
            "quorum": 32,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "information": 'this is the best protocol ever', })

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(Protocol.objects.all()))

    def test_update_user_information(self):
        client.login(username='Kril', password='kril')
        response = client.post('/protocols/add/', {
            "form-TOTAL_FORMS": 2,
            "form-INITIAL_FORMS": 0,
            "form-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "scheduled_time": time(9, 0, 0),
            "start_time": time(10, 0, 0),
            "quorum": 32,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "information": 'this is the best protocol ever', })

        self.assertEqual(200, response.status_code)
        self.assertEqual(1, len(self.kril.attended_meetings()))

    def test_add_protocol_without_being_logged(self):
        response = client.post('/protocols/add/', {
            "form-TOTAL_FORMS": 2,
            "form-INITIAL_FORMS": 0,
            "form-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "scheduled_time": time(9, 0, 0),
            "start_time": time(10, 0, 0),
            "quorum": 32,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "information": 'this is the best protocol ever', })

        self.assertEqual(302, response.status_code)

    def test_add_protocol_with_incomplete_data(self):
        client.login(username='Kril', password='kril')
        response = client.post('/protocols/add/', {
            "form-TOTAL_FORMS": 2,
            "form-INITIAL_FORMS": 0,
            "form-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "start_time": time(10, 0, 0),
            "quorum": 32,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "information": 'this is the best protocol ever', })

        self.assertEqual(200, response.status_code)
        self.assertEqual(0, len(Protocol.objects.all()))

    def test_add_protocols_with_same_numbers(self):
        client.login(username='Kril', password='kril')
        response1 = client.post('/protocols/add/', {
            "form-TOTAL_FORMS": 2,
            "form-INITIAL_FORMS": 0,
            "form-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "information": 'this is the best protocol ever', })

        response2 = client.post('/protocols/add/', {
            "form-TOTAL_FORMS": 2,
            "form-INITIAL_FORMS": 0,
            "form-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "information": 'this is the best protocol ever', })

        self.assertEqual(200, response1.status_code)
        self.assertEqual(200, response2.status_code)
        self.assertEqual(1, len(Protocol.objects.all()))

    def test_user_is_able_to_add_protocols(self):
        client.login(username='Kril', password='kril')
        response1 = client.post('/protocols/add/', {
            "form-TOTAL_FORMS": 2,
            "form-INITIAL_FORMS": 0,
            "form-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "information": 'this is the best protocol ever', })

        self.assertEqual(200, response1.status_code)
        self.assertEqual(1, len(Protocol.objects.all()))

    def test_user_not_able_to_add_protocols(self):
        client.login(username='FakeKril', password='FakeKril')
        response1 = client.post('/protocols/add/', {
            "form-TOTAL_FORMS": 2,
            "form-INITIAL_FORMS": 0,
            "form-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "information": 'this is the best protocol ever', })

        self.assertEqual(302, response1.status_code)
        self.assertEqual(0, len(Protocol.objects.all()))
