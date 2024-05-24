import unittest
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
    def test_create_order(self, mock_save):
        customer_id = fake.customer_id()
        product_id = fake.product_id()
        quantity = fake.quantity()
        total_price = fake.total_price()

        mock_order = MagicMock()
        mock_order.id = 1
        mock_order.customer_id = customer_id
        mock_order.product_id = product_id
        mock_order.quantity = quantity
        mock_order.total_price = total_price        
        mock_save.return_value = mock_order

        payload = {
            "customer_id": customer_id,
            "product_id": product_id,
            "quantity": quantity,
            "total_price": total_price
        }

        response = self.app.post('/orders/', json=payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], mock_order.id)

    def test_missing_customer_id(self, mock_save):
        customer_id = fake.customer_id()
        product_id = fake.product_id()
        quantity = fake.quantity()
        total_price = fake.total_price()

        mock_order = MagicMock()
        mock_order.id = 1
        mock_order.customer_id = customer_id
        mock_order.product_id = product_id
        mock_order.quantity = quantity
        mock_order.total_price = total_price        
        mock_save.return_value = mock_order

        payload = {
            "customer_id": customer_id,
            "product_id": product_id,
            "quantity": quantity,
            "total_price": total_price
        }

        response = self.app.post('/orders/', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('customer_id', response.json)

    def test_missing_product_id(self, mock_save):
        customer_id = fake.customer_id()
        product_id = fake.product_id()
        quantity = fake.quantity()
        total_price = fake.total_price()

        mock_order = MagicMock()
        mock_order.id = 1
        mock_order.customer_id = customer_id
        mock_order.product_id = product_id
        mock_order.quantity = quantity
        mock_order.total_price = total_price        
        mock_save.return_value = mock_order

        payload = {
            "customer_id": customer_id,
            "product_id": product_id,
            "quantity": quantity,
            "total_price": total_price
        }
        response = self.app.post('/orders/', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('product_id', response.json)