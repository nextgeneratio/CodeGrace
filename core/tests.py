from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import TeamMember, Project, Task


class HomeViewTest(TestCase):
    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'CodeGrace')


class TeamMemberModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='alice', password='pass1234')
        self.member = TeamMember.objects.create(user=self.user, role='Backend Developer')

    def test_team_member_str(self):
        self.assertIn('alice', str(self.member))

    def test_team_page_loads(self):
        self.client.login(username='alice', password='pass1234')
        response = self.client.get(reverse('team'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'alice')


class ProjectModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='bob', password='pass1234')
        self.project = Project.objects.create(title='CodeGrace App', description='Hackathon project')
        self.project.members.add(self.user)

    def test_project_str(self):
        self.assertEqual(str(self.project), 'CodeGrace App')

    def test_project_list_requires_login(self):
        response = self.client.get(reverse('project_list'))
        self.assertRedirects(response, '/login/?next=/projects/')

    def test_project_list_authenticated(self):
        self.client.login(username='bob', password='pass1234')
        response = self.client.get(reverse('project_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'CodeGrace App')


class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='carol', password='pass1234')
        self.project = Project.objects.create(title='Sprint 1', description='First sprint')
        self.task = Task.objects.create(
            project=self.project, title='Setup Django', assigned_to=self.user, status='done'
        )

    def test_task_str(self):
        self.assertIn('Setup Django', str(self.task))
        self.assertIn('Done', str(self.task))

    def test_project_detail(self):
        self.client.login(username='carol', password='pass1234')
        response = self.client.get(reverse('project_detail', args=[self.project.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Setup Django')


class AuthTest(TestCase):
    def test_register_creates_team_member(self):
        response = self.client.post(reverse('register'), {
            'username': 'dave',
            'password1': 'Hackath0n!',
            'password2': 'Hackath0n!',
        })
        self.assertRedirects(response, '/')
        self.assertTrue(User.objects.filter(username='dave').exists())
        self.assertTrue(TeamMember.objects.filter(user__username='dave').exists())
