import unittest

from hello import app


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        app.testing = True
        self.client = app.test_client()

    def test_hello(self):
        response = self.client.get('/')
        self.assertEqual(200, response.status_code) # HTTP Response Code 2xx 404 5xx
        self.assertEqual(b'Hello world!', response.data)
