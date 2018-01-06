from django.test import TestCase
from django.shortcuts import resolve_url as r


class HomeTest(TestCase):
    def setUp(self):
        self.reponse = self.client.get(r('home'))

    def test_get(self):
        """ GET / must return status code 200 """
        self.assertEqual(200, self.reponse.status_code)

    def test_template(self):
        """Must use index.html """
        self.assertTemplateUsed(self.reponse, 'index.html')
    
    def test_subscription_link(self):
        expected = 'href="{}'.format(r('subscriptions:new'))
        self.assertContains(self.reponse, expected)

    def test_speakers(self):
        """ Must show keynote speakers """

        contents = [
            'Grace Hopper',
            'http://hbn.link/hopper-pic',
            'Alan Turing',
            'http://hbn.link/turing-pic',
        ]
        for expected in contents:
            with self.subTest():
                self.assertContains(self.reponse, expected)
    
    def test_speakers_link(self):
        expected = 'href="{}#speakers"'.format(r('home'))
        self.assertContains(self.reponse, expected)
    
    def test_nav_links(self):
        contents = [
            'href="{}#overview"'.format(r('home')),
            'href="{}#speakers"'.format(r('home')),
            'href="{}#sponsors"'.format(r('home')),
            'href="{}#register"'.format(r('home')),
            'href="{}#venue"'.format(r('home')),
        ]

        for link in contents:
            with self.subTest():
                self.assertContains(self.reponse, link)
