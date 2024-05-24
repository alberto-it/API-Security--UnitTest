import unittest
from unittest.mock import MagicMock, patch
from app import create_app
from faker import Faker

fake = Faker() 

class TestProductionEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app('DevelopmentConfig')
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    @patch('services.production_service.save')
    def test_create_production(self, mock_save):
        product_id = fake.product_id()
        quantity_produced = fake.quantity_produced()
        date_produced = fake.date_produced()

        mock_production = MagicMock()
        mock_production.id = 1
        mock_production.product_id = product_id
        mock_production.quantity_produced = quantity_produced
        mock_production.date_produced = date_produced        
        mock_save.return_value = mock_production

        payload = {
            "product_id": product_id,
            "quantity_produced": quantity_produced,
            "date_produced": date_produced
        }

        response = self.app.post('/productions/', json=payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], mock_production.id)

    def test_missing_product_id(self, mock_save):
        product_id = fake.product_id()
        quantity_produced = fake.quantity_produced()
        date_produced = fake.date_produced()

        mock_production = MagicMock()
        mock_production.id = 1
        mock_production.product_id = product_id
        mock_production.quantity_produced = quantity_produced
        mock_production.date_produced = date_produced        
        mock_save.return_value = mock_production

        payload = {
            "product_id": product_id,
            "quantity_produced": quantity_produced,
            "date_produced": date_produced
        }

        response = self.app.post('/productions/', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('product_id', response.json)

    def test_missing_date_produced(self, mock_save):
        product_id = fake.product_id()
        quantity_produced = fake.quantity_produced()
        date_produced = fake.date_produced()

        mock_production = MagicMock()
        mock_production.id = 1
        mock_production.product_id = product_id
        mock_production.quantity_produced = quantity_produced
        mock_production.date_produced = date_produced        
        mock_save.return_value = mock_production

        payload = {
            "product_id": product_id,
            "quantity_produced": quantity_produced,
            "date_produced": date_produced
        }

        response = self.app.post('/productions/', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('date_produced', response.json)