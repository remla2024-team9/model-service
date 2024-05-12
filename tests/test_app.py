from src.app import app
import unittest

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_predict_endpoint(self):
        response = self.client.post('/predict', json={'data': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('received', str(response.data))

if __name__ == "__main__":
    unittest.main()
