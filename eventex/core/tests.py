from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.reponse = self.client.get('/')

    def test_get(self):
        """ GET / must return status code 200 """
        self.assertEqual(200, self.reponse.status_code)

    def test_template(self):
        """Must use index.html """
        self.assertTemplateUsed(self.reponse, 'index.html')
