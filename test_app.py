import app
import unittest

class AppTestCase(unittest.TestCase):
    def setUp(self):
        app.app.testing = True  # enable testing mode
        self.client = app.app.test_client()

    def test_homepage(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Accessify Lite', response.data)  # or some expected text in homepage

if __name__ == '__main__':
    unittest.main()


