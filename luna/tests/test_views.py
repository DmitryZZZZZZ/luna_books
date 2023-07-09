from django.test import TestCase


class LunaHomeViewTestCase(TestCase):
    def test_url_main_page_status_code(self):
        resp = self.client.get('')
        self.assertEqual(resp.status_code, 200)


    def test_context_in_data_mixin(self):
        resp = self.client.get('')
        self.assertTrue('menu' in resp.context)
        self.assertTrue('cats' in resp.context)

    def test_correct_template(self):
        resp = self.client.get('')
        self.assertTemplateUsed(resp, 'luna/index.html')