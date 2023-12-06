import unittest
from flask.wrappers import Response

from flask_app import app


class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_home_route(self):
        response: Response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Home", response.data)

    def test_traits_route(self):
        response: Response = self.client.get("/traits")
        self.assertEqual(response.status_code, 200)

    def test_predict_route(self):
        response: Response = self.client.post(
            "/predict", data={"prompt": "programming"}
        )
        self.assertEqual(response.status_code, 302)
        self.assertIn(b"Redirecting", response.data)

    def test_result_route(self):
        response: Response = self.client.get("/result")
        self.assertEqual(response.status_code, 200)

    def test_get_top_professions(self):
        traits = "programming"
        result = app.get_top_professions(traits)
        self.assertIsInstance(result, str)


if __name__ == "__main__":
    unittest.main()
