from django.contrib.auth.models import Permission
from django.test import TestCase, client

from members.models import User
from .models import Position


client_obj_inst = client.Client()


class PositionTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin', faculty_number='7023')
        self.user.set_password('admin')
        self.user.save()

        perm = Permission.objects.get(codename='add_position')
        self.user.user_permissions.add(perm)
        self.not_master = User.objects.create(username='not_master',
                                              faculty_number='7702')
        self.not_master.set_password('not_master')
        self.not_master.save()


    def test_add_new_position_with_right_permissions(self):
        client_obj_inst.login(username='admin', password='admin')
        before_add = Position.objects.count()
        response = client_obj_inst.post('/positions/add/', {
            'title': 'Position title',
            'content': 'texttttttttt'})
        after_add = Position.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(before_add+1, after_add)


    def test_add_new_position_with_right_permissions_and_form_errors(self):
        client_obj_inst.login(username='admin', password='admin')
        before_add = Position.objects.count()
        response = client_obj_inst.post('/positions/add/', {
            'title': '',
            'content': ''})
        after_add = Position.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(before_add, after_add)


    def test_add_new_position_with_no_permissions(self):
        client_obj_inst.login(username='not_master', password='not_master')
        before_add = Position.objects.count()
        response = client_obj_inst.post('/positions/add/', {
            'title': 'Position title',
            'content': 'texttttttttt'})
        after_add = Position.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(before_add, after_add)
