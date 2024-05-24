import unittest
from unittest.mock import MagicMock, patch
from app import create_app
from faker import Faker

fake = Faker()

class TestProductEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app('DevelopmentConfig')
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    @patch('services.product_service.save')
    def test_create_product(self, mock_save):
        name = fake.name()
        price = fake.price()
        mock_product = MagicMock()
        mock_product.id = 1
        mock_product.name = name
        mock_product.price = price
        mock_save.return_value = mock_product

        payload = {
            "name": name,
            "price": price
        }

        response = self.app.post('/products/', json=payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], mock_product.id)

    def test_missing_name(self, mock_save):
        name = fake.name()
        price = fake.position()
        mock_product = MagicMock()
        mock_product.id = 1
        mock_product.name = name
        mock_product.price = price
        mock_save.return_value = mock_product

        payload = {
            "name": name,
            "price": price
        }

        response = self.app.post('/products/', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('name', response.json)

    def test_missing_price(self, mock_save):
        name = fake.name()
        price = fake.position()
        mock_product = MagicMock()
        mock_product.id = 1
        mock_product.name = name
        mock_product.price = price
        mock_save.return_value = mock_product

        payload = {
            "name": name,
            "price": price
        }

        response = self.app.post('/products/', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('price', response.json)