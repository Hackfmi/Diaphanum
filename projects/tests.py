from django.contrib.auth.models import Permission
from django.test import TestCase, client


from members.models import User
from .models import Project


client = client.Client()


class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='admin', faculty_number='7023')
        self.user.set_password('admin')
        self.user.save()

        perm = Permission.objects.get(codename='change_project')
        self.user.user_permissions.add(perm)

        self.not_master = User.objects.create(username='not_master',
                                              faculty_number='7702')
        self.not_master.set_password('not_master')
        self.not_master.save()

    def test_add_new_project(self):
        client.login(username='admin', password='admin')
        before_add = Project.objects.count()
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
        after_add = Project.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(before_add + 1, after_add)

    def test_adding_new_project_from_user_who_is_not_logged(self):
        before_add = Project.objects.count()
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
        after_add = Project.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(before_add, after_add)

    def test_adding_incomplete_project(self):
        client.login(username='admin', password='admin')
        before_add = Project.objects.count()
        response = client.post('/projects/add/', {
            'team': [self.user.pk],
            'name': 'New project',
            'description': 'spam',
            'target_group': 'spam',
            'schedule': 'spam',
            'resources': 'spam',
            'finance_description': 'spam'})
        after_add = Project.objects.count()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(before_add, after_add)

    def test_edit_status_of_project_user_has_permissions(self):
        client.login(username='admin', password='admin')
        inst = Project.objects.create(
            user=self.not_master,
            flp=self.user,
            name='New project',
            description='spam',
            tasks='spam',
            targets='spam',
            target_group='spam',
            schedule='spam',
            resources='spam',
            finance_description='spam')
        before_add = Project.objects.count()
        response = client.post('/projects/edit_status/{}/'.format(inst.pk), {
                                'status': 'approved'})
        after_add = Project.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(before_add, after_add)

    def test_edit_project_from_its_creator(self):
        client.login(username='not_master', password='not_master')
        inst = Project.objects.create(
                        user=self.not_master,
                        flp=self.user,
                        name='New project',
                        description='spam',
                        tasks='spam',
                        targets='spam',
                        target_group='spam',
                        schedule='spam',
                        resources='spam',
                        finance_description='spam',
                        status='unrevised',)
        before_add = Project.objects.count()

        response = client.post('/projects/edit/{}/'.format(inst.pk), {
                                'name': 'some other name'})
        after_add = Project.objects.count()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(before_add, after_add)

    def test_edit_project_impossible_from_this_user(self):
        '''this user is not the creator of the project'''

        client.login(username='not_master', password='not_master')
        inst = Project.objects.create(
                        user=self.user,
                        flp=self.not_master,
                        name='New project',
                        description='spam',
                        tasks='spam',
                        targets='spam',
                        target_group='spam',
                        schedule='spam',
                        resources='spam',
                        finance_description='spam')
        before_add = Project.objects.count()
        response = client.post('/projects/edit/{}/'.format(inst.pk), {
                                'name': 'some other name'})
        after_add = Project.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(before_add, after_add)

    def test_change_status_impossible_from_this_user(self):
        '''this user is the project creator, but cannot edit its status'''

        client.login(username='not_master', password='not_master')
        inst = Project.objects.create(
                        user=self.not_master,
                        flp=self.user,
                        name='New project',
                        description='spam',
                        tasks='spam',
                        targets='spam',
                        target_group='spam',
                        schedule='spam',
                        resources='spam',
                        finance_description='spam')
        before_add = Project.objects.count()
        response = client.post('/projects/edit_status/{}/'.format(inst.pk), {
                               'status': 'approved'})
        after_add = Project.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(before_add, after_add)

    def test_edit_project_with_not_logged_in_user(self):
        inst = Project.objects.create(
                    user=self.not_master,
                    flp=self.user,
                    name='New project',
                    description='spam',
                    tasks='spam',
                    targets='spam',
                    target_group='spam',
                    schedule='spam',
                    resources='spam',
                    finance_description='spam')
        before_add = Project.objects.count()
        response = client.post('/projects/edit/{}/'.format(inst.pk), {
                                'name': 'some other name'})
        after_add = Project.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(before_add, after_add)

    def test_master_can_edit_status(self):
        client.login(username='admin', password='admin')
        inst = Project.objects.create(
                    user=self.not_master,
                    flp=self.not_master,
                    name='New project',
                    description='spam',
                    tasks='spam',
                    targets='spam',
                    target_group='spam',
                    schedule='spam',
                    resources='spam',
                    finance_description='spam')
        before_add = Project.objects.count()
        response = client.post('/projects/edit_status/{}/'.format(inst.pk), {
                               'status': 'rejected'})
        after_add = Project.objects.count()
        self.assertEqual(response.status_code, 302)
        self.assertEqual(before_add, after_add)

    def test_master_cannot_edit_project(self):
        client.login(username='admin', password='admin')

        Project.objects.create(
            user=self.not_master,
            flp=self.not_master,
            name='New project',
            description='spam',
            tasks='spam',
            targets='spam',
            target_group='spam',
            schedule='spam',
            resources='spam',
            finance_description='spam')

        response = client.post('/projects/edit/{}/'.format(inst.pk), {
                                'name': 'other project name'})
        after_edit = Project.objects.filter(name='other project name')
        self.assertEqual(response.status_code, 302)
        self.assertEqual(0, len(after_edit))

    def test_show_projects_archive(self):
        client.login(username='admin', password='admin')
        for project_number in range(10):
            instance = Project.objects.create(
                user=self.not_master,
                flp=self.not_master,
                name='Project{}'.format(project_number),
                description='spam',
                tasks='spam',
                targets='spam',
                target_group='spam',
                schedule='spam',
                resources='spam',
                finance_description='spam')

            if project_number < 4:
                client.post('/projects/edit_status/{}/'.format(instance.pk), {
                                'status': 'approved'})

        response = client.get('/projects/archive/')

        self.assertEqual(200, response.status_code)
        self.assertEqual(6, len(response.context['unrevised']))
        self.assertEqual(4, len(response.context['approved']))

    def test_show_project_by_id(self):
        pass

    def test_show_project_versions(self):
        pass

    def test_projects_by_month_and_year(self):
        pass
