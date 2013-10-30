# -*- coding: utf-8 -*-
from django.test import TestCase, client

from .models import Feedback


client = client.Client()


class FeedbackTest(TestCase):
    def test_add_feedback(self):
        pass
        # before_add = Feedback.objects.count()
        # response = client.post('/feedback/add/', {
        #     'name': 'Пандо Пандев',
        #     'email': 'panda@panda.com',
        #     'information': 'Тука се разхожда една панда по екрана'})
        # after_add = Feedback.objects.count()
        # self.assertEqual(response.status_code, 302)
        # self.assertEqual(before_add + 1, after_add)

    def test_user_add_feedback(self):
        pass
