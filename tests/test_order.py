import unittest, datetime
from unittest.mock import MagicMock, patch
from app import create_app
from faker import Faker

fake = Faker() 

class TestOrderEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app('DevelopmentConfig')
        app.config['TESTING'] = True
        self.app = app.test_client()

    @patch('services.order_service.save')
    def test_missing_customer_id(self, mock_save):
        product_id = fake.random_number()
        mock_order = MagicMock()
        mock_order.id = 1
        mock_order.product_id = product_id
        mock_save.return_value = mock_order

        payload = {
            "products": [
                {
                    "id": product_id,
                }
            ]
        }

        response = self.app.post('/orders/', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('customer_id', response.json)