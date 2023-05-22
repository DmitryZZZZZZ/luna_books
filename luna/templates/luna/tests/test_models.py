from django.test import TestCase

from luna.models import Post, Category, Contact


class PostModelTestCase(TestCase):
    def test_get_absolute_url(self):
        post = Post(title="New", content="Content", slug='New')
        self.assertEqual(post.get_absolute_url(), f"/post/{post.slug}/")


class CategoryModelTestCase(TestCase):
    def test_get_absolute_url(self):
        category = Category(name="Книги на русском языке",
                            slug='Knigi_na_russkom_yazyke')
        self.assertEqual(category.get_absolute_url(), f"/category/{category.slug}/")


class ContactModelTestCase(TestCase):
    def test_absolute_url(self):
        self.assertEqual(Contact.get_absolute_url(self), '/contact/')

    def test_model_field_label(self):
        Contact.objects.create(first_name='Fedor', last_name='Melnikov',
                               email='melnik444@mail.ru', message='tesе messsage')
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('first_name').verbose_name
        self.assertEqual(field_label, 'Имя')

    def test_model_max_length(self):
        Contact.objects.create(first_name='Fedor', last_name='Melnikov',
                               email='melnik444@mail.ru', message='test messsage')
        contact = Contact.objects.get(id=1)
        field_label = contact._meta.get_field('message').max_length
        self.assertEqual(field_label, 1000)

    def test_object_name_is_first_name(self):
        Contact.objects.create(first_name='Fedor', last_name='Melnikov', email='melnik444@mail.ru',
                               message='test messsage')
        contact = Contact.objects.get(id=1)
        expected_object_name = contact.first_name
        self.assertEquals(expected_object_name, contact.first_name)
