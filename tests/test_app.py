import unittest

from app import create_app


class CreateAppTests(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index_page_renders(self) -> None:
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        html = response.get_data(as_text=True)
        self.assertIn('Image processing workspace boilerplate', html)
        self.assertIn('Bootstrap 5 base template', html)

    def test_health_endpoint_returns_ok(self) -> None:
        response = self.client.get('/health')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'status': 'ok'})


if __name__ == '__main__':
    unittest.main()
