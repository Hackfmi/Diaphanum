from django.test import client, TestCase

from members.models import User
from datetime import time
from django.contrib.auth.models import Permission
from .models import Report, Copy
from protocols.models import Topic, Institution, Protocol


client = client.Client()


class ReportTest(TestCase):
    def setUp(self):
        self.kril = User.objects.create(
            username='Kril',
            faculty_number='61277',
            email='kril@gmail.com',)
        self.kril.set_password('kril')
        self.kril.save()
        perm = Permission.objects.get(codename='add_report')
        self.kril.user_permissions.add(perm)

        self.fake_kril = User.objects.create(
            username='FakeKril',
            faculty_number='80460',
            email='kril@kril.kril',)
        self.kril.set_password('FakeKril')
        self.fake_kril.save()

        self.institution = Institution.objects.create(
            name='some institution name')

        self.protocol = Protocol.objects.create(
            institution=self.institution,
            number='2341',
            scheduled_time=time(9, 0, 0),
            start_time=time(10, 0, 0),
            quorum=32,
            majority=5,
            current_majority=4,
            information="best protocol ever",
            )

        self.topic1 = Topic.objects.create(
            name='1',
            voted_for=13,
            voted_against=4,
            voted_abstain=5,
            protocol=self.protocol)
        self.topic2 = Topic.objects.create(
            name='2',
            voted_for=13,
            voted_against=4,
            voted_abstain=5,
            protocol=self.protocol)
        self.topic3 = Topic.objects.create(
            name='3',
            voted_for=13,
            voted_against=4,
            voted_abstain=5,
            protocol=self.protocol)

    def test_add_report_no_copies(self):
        client.login(username='Kril', password='kril')
        before_add = Report.objects.count()
        response = client.post('/reports/add/', {
            "copies-TOTAL_FORMS": 2,
            "copies-INITIAL_FORMS": 0,
            "copies-MAX_NUM_FORMS": 1000,
            "addressed_to": "Hackfmi",
            "reported_from": self.kril.pk,
            "content": "This is a report test",
            "signed_from": "rozovo zaiche", })

        after_add = Report.objects.count()

        self.assertEqual(200, response.status_code)
        self.assertEqual(before_add + 1, after_add)

    def test_add_report_with_incomplete_data(self):
        copies_before_add = Copy.objects.count()
        before_add = Report.objects.count()
        client.login(username='Kril', password='kril')
        response = client.post('/reports/add/', {
            "copies-TOTAL_FORMS": 2,
            "copies-INITIAL_FORMS": 0,
            "copies-MAX_NUM_FORMS": 1000,
            "addressed_to": "Hackfmi",
            "reported_from": self.kril.pk,
            "content": "This is a report test",
            "copies-0-about_topic": self.topic1.pk,
            "copies-1-about_topic": self.topic2.pk,

            })
        after_add = Report.objects.count()
        copies_after_add = Copy.objects.count()
        self.assertEqual(200, response.status_code)
        self.assertEqual(before_add, after_add)
        self.assertEqual(copies_before_add, copies_after_add)

    def test_user_reports_count_1(self):
        before_add = Report.objects.count()
        client.login(username='Kril', password='kril')
        response = client.post('/reports/add/', {
            "copies-TOTAL_FORMS": 2,
            "copies-INITIAL_FORMS": 0,
            "copies-MAX_NUM_FORMS": 1000,
            "addressed_to": "Hackfmi",
            "reported_from": self.kril.pk,
            "content": "This is a report test",
            "signed_from": "rozovo zaiche", })
        after_add = Report.objects.count()

        self.assertEqual(200, response.status_code)
        self.assertEqual(before_add + 1, after_add)

    def test_user_reports_count_2(self):
        before_add = Report.objects.count()
        copies_before_add = Copy.objects.count()
        client.login(username='Kril', password='kril')
        response = client.post('/reports/add/', {
            "copies-TOTAL_FORMS": 2,
            "copies-INITIAL_FORMS": 0,
            "copies-MAX_NUM_FORMS": 1000,
            "addressed_to": "Hackfmi",
            "reported_from": self.kril.pk,
            "content": "This is a report test",
            "copies-0-about_topic": self.topic1.pk,
            "copies-1-about_topic": self.topic2.pk,
            "signed_from": "rozovo zaiche", })

        self.assertEqual(200, response.status_code)

        response = client.post('/reports/add/', {
            "copies-TOTAL_FORMS": 2,
            "copies-INITIAL_FORMS": 0,
            "copies-MAX_NUM_FORMS": 1000,
            "addressed_to": "Hackfmi",
            "reported_from": self.kril.pk,
            "content": "This is a report test",
            "signed_from": "rozovo zaiche", })
        after_add = Report.objects.count()
        copies_after_add = Copy.objects.count()
        self.assertEqual(200, response.status_code)
        self.assertEqual(before_add + 2, after_add)
        self.assertEqual(copies_before_add + 2, copies_after_add)

    def test_user_is_spamer(self):
        copies_before_add = Copy.objects.count()
        before_add = Report.objects.count()
        client.login(username='Kril', password='kril')
        for report in range(10):
            response = client.post('/reports/add/', {
                "copies-TOTAL_FORMS": 2,
                "copies-INITIAL_FORMS": 0,
                "copies-MAX_NUM_FORMS": 1000,
                "addressed_to": "Hackfmi",
                "reported_from": self.kril.pk,
                "content": "This is a report test",
                "signed_from": "rozovo zaiche", })

        copies_after_add = Copy.objects.count()
        self.assertEqual(200, response.status_code)
        after_add = Report.objects.count()
        self.assertEqual(before_add + 10, after_add)
        self.assertEqual(copies_before_add, copies_after_add)

    def test_unauthorised_to_report_user(self):
        before_add = Report.objects.count()
        client.login(username='FakeKril', password='FakeKril')
        for report in range(10):
            response = client.post('/reports/add/', {
                "copies-TOTAL_FORMS": 2,
                "copies-INITIAL_FORMS": 0,
                "copies-MAX_NUM_FORMS": 1000,
                "addressed_to": "Hackfmi",
                "reported_from": self.kril.pk,
                "content": "This is a report test",
                "signed_from": "rozovo zaiche", })

        after_add = Report.objects.count()
        self.assertEqual(302, response.status_code)
        self.assertEqual(before_add, after_add)

    def test_listing_page_of_reports(self):
        before_add = Report.objects.count()
        copies_before_add = Copy.objects.count()
        client.login(username='Kril', password='kril')
        for report in range(10):
            response = client.post('/reports/add/', {
                "copies-TOTAL_FORMS": 2,
                "copies-INITIAL_FORMS": 0,
                "copies-MAX_NUM_FORMS": 1000,
                "addressed_to": "Hackfmi",
                "reported_from": self.kril.pk,
                "content": "This is a report test",
                "copies-0-about_topic": self.topic1.pk,
                "copies-1-about_topic": self.topic2.pk,
                "copies-2-about_topic": self.topic3.pk,
                "signed_from": "rozovo zaiche", })

        response = client.get('/reports/archive/1/')

        after_add = Report.objects.all().count()
        copies_after_add = Copy.objects.count()

        self.assertEqual(200, response.status_code)
        self.assertEqual(before_add + 10, after_add)
        self.assertEqual(copies_before_add + 20, copies_after_add)
        self.assertEqual(after_add, len(response.context['reports']))
