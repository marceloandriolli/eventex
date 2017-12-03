from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        obj = Subscription.objects.create(
            name='Marcelo Andriolli',
            cpf='12345678901',
            email='marcelorsa@gmail.com',
            phone='48-996274443'
        )
        self.resp = self.client.get('/inscricao/{}/'.format(obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)
    
    def test_template(self):
        self.assertTemplateUsed(self.resp, 
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = ('Marcelo Andriolli', '12345678901',
                     'marcelorsa@gmail.com', '48-996274443')
        
        with self.subTest():
            for expected in contents:
                self.assertContains(self.resp, expected) 


class SubscriptionDetailNorFound(TestCase):
    
    def test_not_found(self):
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(404, resp.status_code)
