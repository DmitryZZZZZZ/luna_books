from django.test import TestCase
from luna.forms import AddPostForm
import unittest


class PostFormTestCase(TestCase):
    def test_valid_form_label(self):
        form = AddPostForm()
        self.assertEqual(form.fields['title'].label, 'Заголовок')

    def test_empty_label(self):
        form = AddPostForm()
        self.assertEqual(form.fields['cat'].empty_label, 'Категория не выбрана')




