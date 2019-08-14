from django.test import TestCase
from .service_module import generate_shorted_url, get_random_urlstring


class UrlShortenerTest(TestCase):

    def test_should_short_url(self):
        url = "www.yahoo.com"
        res = generate_shorted_url(url)
        self.assertIsNotNone(res)
        self.assertIsNotNone(res.shortened_url)
        self.assertEqual(url, res.original_url)

    def test_should_create_random_string_as_shortener(self):
        expected_len = 500
        res = get_random_urlstring(expected_len)
        self.assertIsNotNone(res)
        self.assertEqual(len(res), expected_len)
