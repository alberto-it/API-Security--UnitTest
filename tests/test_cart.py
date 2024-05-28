import unittest, datetime
from unittest.mock import MagicMock, patch
from app import create_app
from faker import Faker

fake = Faker()

class TestCartEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app('DevelopmentConfig')
        app.config['TESTING'] = True
        self.app = app.test_client()

    @patch('services.cart_service.ShoppingCartService.save')
    def test_missing_customer_id(self, mock_save):
        customer_id = fake.random_int()
        product_id = fake.random_int()
        quantity = fake.random_int()
        mock_order = MagicMock()
        mock_order.id = 1
        mock_order.customer_id = customer_id
        mock_order.product_id = product_id
        mock_order.quantity = quantity
        mock_save.return_value = mock_order

        payload = {
            "products": [
                {
                    "id": product_id,
                    "quantity": quantity
                }
            ]
        }

        response = self.app.post('/orders/', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('customer_id', response.json)