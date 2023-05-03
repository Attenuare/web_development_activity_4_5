from django.test import TestCase


class HomePageTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_200_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_text(self):
        self.assertContains(self.response, 'Insira a data:')

    def test_templates_home(self):
        self.assertTemplateUsed(self.response, 'list_schedule.html')

class ListPageTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/?schedule=2023-05-10')

    def test_200_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_text(self):
        self.assertContains(self.response, 'Encontrada(s)') 

class RegisterPageTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/schedule')

    def test_200_response(self):
        self.assertEqual(self.response.status_code, 200)

    def test_text(self):
        self.assertContains(self.response, 'Registrar Tarefa')

    def test_templates_home(self):
        self.assertTemplateUsed(self.response, 'register_schedule.html')
