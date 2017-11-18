from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Marcelo Andriolli', cpf='12345678901',
                    email='marcelorsa@gmail.com', phone='48-996274443')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]
    
    def test_send_subscribe_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)
    
    def test_send_subscribe_email_from(self):
        expect = 'contato@eventex.com.br'

        self.assertEqual(expect, self.email.from_email)

    def test_send_subscribe_email_to(self):
        expect = ['contato@eventex.com.br', 'marcelorsa@gmail.com']

        self.assertEqual(expect, self.email.to)

    def test_send_subscribe_email_body(self):
        contents = [
            'Marcelo Andriolli',
            '12345678901',
            'marcelorsa@gmail.com',
            '48-996274443'
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
