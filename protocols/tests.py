# -*- encoding:utf-8 -*-
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
        perm = Permission.objects.get(codename='add_protocol')
        self.kril.user_permissions.add(perm)

        self.fake_kril = User.objects.create(
            username='FakeKril',
            faculty_number='80460',
            email='kril@kril.kril',)
        self.kril.set_password('FakeKril')
        self.fake_kril.save()

        self.institution = Institution.objects.create(name='SO')

        self.institution2 = Institution.objects.create(name='СИС')

    def tearDown(self):
        Protocol.objects.all().delete()

    def test_add_protocol(self):
        client.login(username='Kril', password='kril')
        before_add = Protocol.objects.count()
        response = client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 2,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "scheduled_time": time(9, 0, 0),
            "start_time": time(10, 0, 0),
            "quorum": 32,
            "absent": self.kril.pk,
            "excused": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever', })

        after_add = Protocol.objects.count()
        self.assertEqual(200, response.status_code)
        self.assertEqual(before_add + 1, after_add)

    def test_update_user_information(self):
        client.login(username='Kril', password='kril')
        before_add = Protocol.objects.count()
        response = client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 2,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "scheduled_time": time(9, 0, 0),
            "start_time": time(10, 0, 0),
            "quorum": 32,
            "excused": self.kril.pk,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever', })
        after_add = Protocol.objects.count()

        self.assertEqual(200, response.status_code)
        self.assertEqual(before_add + 1, after_add)

    def test_add_protocol_without_being_logged(self):
        response = client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 2,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "scheduled_time": time(9, 0, 0),
            "start_time": time(10, 0, 0),
            "quorum": 32,
            "excused": self.kril.pk,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever', })

        self.assertEqual(302, response.status_code)

    def test_add_protocol_with_incomplete_data(self):
        before_add = Protocol.objects.count()
        client.login(username='Kril', password='kril')
        response = client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 2,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "start_time": time(10, 0, 0),
            "quorum": 32,
            "excused": self.kril.pk,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever', })
        after_add = Protocol.objects.count()

        self.assertEqual(200, response.status_code)
        self.assertEqual(before_add, after_add)

    def test_add_protocols_with_same_numbers(self):
        before_add = Protocol.objects.count()
        client.login(username='Kril', password='kril')
        response1 = client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 2,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "excused": self.kril.pk,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever', })

        response2 = client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 2,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "excused": self.kril.pk,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever', })

        after_add = Protocol.objects.count()

        self.assertEqual(200, response1.status_code)
        self.assertEqual(200, response2.status_code)
        self.assertEqual(before_add + 1, after_add)

    def test_user_is_able_to_add_protocols(self):
        before_add = Protocol.objects.count()
        client.login(username='Kril', password='kril')
        response1 = client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 2,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "excused": self.kril.pk,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever', })
        after_add = Protocol.objects.count()

        self.assertEqual(200, response1.status_code)
        self.assertEqual(before_add + 1, after_add)

    def test_user_not_able_to_add_protocols(self):
        before_add = Protocol.objects.count()
        client.login(username='FakeKril', password='FakeKril')
        response1 = client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 2,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "excused": self.kril.pk,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever', })
        after_add = Protocol.objects.count()

        self.assertEqual(302, response1.status_code)
        self.assertEqual(before_add, after_add)

    def test_add_protocol_with_topic(self):
        before_add = Protocol.objects.count()
        topics_count_before = Topic.objects.count()
        client.login(username='Kril', password='kril')
        response = client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 1,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "excused": self.kril.pk,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever',
            "topics-0-name": "topic",
            "topics-0-voted_for": 4,
            "topics-0-voted_against": 4,
            "topics-0-voted_abstain": 4,
            "topics-0-statement": "4", })
        topics_count_after = Topic.objects.count()
        after_add = Protocol.objects.count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(before_add + 1, after_add)
        self.assertEqual(topics_count_before + 1, topics_count_after)

    def test_add_protocol_with_two_topics(self):
        before_add = Protocol.objects.count()
        topics_count_before = Topic.objects.count()
        client.login(username='Kril', password='kril')
        response = client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 2,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1234",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "excused": self.kril.pk,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever',
            "topics-0-name": "topic",
            "topics-0-voted_for": 4,
            "topics-0-voted_against": 4,
            "topics-0-voted_abstain": 4,
            "topics-0-statement": "4",
            "topics-1-name": "topic2",
            "topics-1-voted_for": 4,
            "topics-1-voted_against": 4,
            "topics-1-voted_abstain": 4,
            "topics-1-statement": "4", })

        after_add = Protocol.objects.count()
        topic = Topic.objects.filter(name="topic", statement="4").exists()
        topics_count_after = Topic.objects.count()
        self.assertEqual(200, response.status_code)
        self.assertEqual(before_add + 1, after_add)
        self.assertTrue(topic)
        self.assertEqual(topics_count_before + 2, topics_count_after)

    def test_search_institution_in_bg(self):
        response = client.get('/protocols/search/{}/'.format(self.institution2.name))
        self.assertEqual(200, response.status_code)
        self.assertTrue(response.content)

    def test_institution_not_found(self):
        response = client.get('/protocols/search/pe/')
        self.assertEqual(200, response.status_code)
        self.assertEqual(response.content, '[]')

    def test_listing_page_of_protocols(self):
        before_add = Protocol.objects.count()
        client.login(username='Kril', password='kril')
        client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 2,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "1234",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "excused": self.kril.pk,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever', })

        client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 2,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "13/11/1992/1235",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "excused": self.kril.pk,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever', })

        response = client.get('/protocols/archive/1/')

        after_add = Protocol.objects.count()
        self.assertEqual(200, response.status_code)
        self.assertEqual(before_add + 2, after_add)
        self.assertEqual(after_add, len(response.context['protocols']))

    def test_listing_page_of_protocols_with_over_30_protocols(self):
        before_add = Protocol.objects.count()
        client.login(username='Kril', password='kril')
        for add_protocol in range(35):
            client.post('/protocols/add/', {
                "topics-TOTAL_FORMS": 2,
                "topics-INITIAL_FORMS": 0,
                "topics-MAX_NUM_FORMS": 1000,
                "institution": self.institution.pk,
                "number": "{}".format(add_protocol),
                "start_time": time(10, 0, 0),
                "scheduled_time": time(9, 0, 0),
                "quorum": 32,
                "excused": self.kril.pk,
                "absent": self.kril.pk,
                "attendents": self.kril.pk,
                "majority": 5,
                "current_majority": 4,
                "voted_for": 2,
                "voted_against": 3,
                "voted_abstain": 0,
                "information": 'this is the best protocol ever', })

        response_1 = client.get('/protocols/archive/1/')
        response_2 = client.get('/protocols/archive/2/')

        after_add = Protocol.objects.count()
        self.assertEqual(200, response_1.status_code)
        self.assertEqual(200, response_2.status_code)
        self.assertEqual(before_add + 35, after_add)
        self.assertEqual(30, len(response_1.context['protocols']))
        self.assertEqual(5, len(response_2.context['protocols']))

    def test_display_protocol_by_id(self):
        client.login(username='Kril', password='kril')
        c_post = client.post('/protocols/add/', {
            "topics-TOTAL_FORMS": 2,
            "topics-INITIAL_FORMS": 0,
            "topics-MAX_NUM_FORMS": 1000,
            "institution": self.institution.pk,
            "number": "1234",
            "start_time": time(10, 0, 0),
            "scheduled_time": time(9, 0, 0),
            "quorum": 32,
            "excused": self.kril.pk,
            "absent": self.kril.pk,
            "attendents": self.kril.pk,
            "majority": 5,
            "current_majority": 4,
            "voted_for": 2,
            "voted_against": 3,
            "voted_abstain": 0,
            "information": 'this is the best protocol ever', })
        response = client.get('/protocols/archive/review/{}/'.format(
                                                c_post.context['protocol'].pk))

        self.assertEqual(200, response.status_code)
