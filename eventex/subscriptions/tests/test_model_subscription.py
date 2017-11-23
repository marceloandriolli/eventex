from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Marcelo Andriolli',
            cpf='12345678901',
            email='marcelorsa@gmail.com',
            phone='48-996274443'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """ Subscription must have an auto created_at attribute """
        self.assertIsInstance(self.obj.created_at, datetime)