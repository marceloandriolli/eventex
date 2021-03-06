from django.test import TestCase
from eventex.core.models import Talk, Course, Course
from eventex.core.managers import PeriodManager

class TalkModelTest(TestCase):
    def setUp(self):
        self.talk = Talk.objects.create(
            title = 'Título da palestra'
        )
    
    def test_create(self):
        self.assertTrue(Talk.objects.exists())
    
    def test_has_speaker(self):
        """ Talk has many speakers and vice-versa """
        self.talk.speakers.create(
            name='Marcelo Andriolli',
            slug='henrique-bastos',
            website='http://marceloandriolli.net'
        )
        self.assertEqual(1, self.talk.speakers.count())
    
    def test_description_black(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speakers_black(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)
    
    def test_start_black(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)
    
    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da palestra', str(self.talk))
    
    def test_ordering(self):
        self.assertListEqual(['start'], Talk._meta.ordering)


class PeriodManagerTest(TestCase):
    def setUp(self):
        Talk.objects.create(title='Morning Talk', start='11:59')
        Talk.objects.create(title='Afternoon Talk', start='12:00')
    
    def test_manager(self):
        self.assertIsInstance(Talk.objects, PeriodManager)

    def test_at_morning(self):
        qs = Talk.objects.at_morning()
        expected = ['Morning Talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)

    def test_at_afternoon(self):
        qs = Talk.objects.at_afternoon()
        expected = ['Afternoon Talk']
        self.assertQuerysetEqual(qs, expected, lambda o: o.title)


class CourseModelTest(TestCase):
    def setUp(self):
        self.Course = Course.objects.create(
            title='Título do Curso',
            start='09:00',
            description='Descrição do curso.',
            slots=20
        )

    def test_create(self):
        self.assertTrue(Course.objects.exists())
    
    def test_speaker(self):
        """Course has many speakers and vice-versa """
        self.Course.speakers.create(
            name='Marcelo Andriolli',
            slug='marcelo-andriolli',
            website='http://marceloandriolli.net' 
        )

        self.assertEqual(1, self.Course.speakers.count())

    def test_str(self):
        self.assertEqual('Título do Curso', str(self.Course))
    
    def test_manager(self):
        self.assertIsInstance(Course.objects, PeriodManager)

    def test_ordering(self):
        self.assertListEqual(['start'], Course._meta.ordering)