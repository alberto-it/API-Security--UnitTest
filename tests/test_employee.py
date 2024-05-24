import unittest
from unittest.mock import MagicMock, patch
from app import create_app
from faker import Faker

fake = Faker()

class TestEmployeeEndpoints(unittest.TestCase):
    def setUp(self):
        app = create_app('DevelopmentConfig')
        app.config['TESTING'] = True
        self.app = app.test_client()
    
    @patch('services.employee_service.save')
    def test_create_employee(self, mock_save):
        name = fake.name()
        position = fake.position()
        mock_employee = MagicMock()
        mock_employee.id = 1
        mock_employee.name = name
        mock_employee.position = position
        mock_save.return_value = mock_employee

        payload = {
            "name": name,
            "position": position
        }

        response = self.app.post('/employees/', json=payload)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['id'], mock_employee.id)

    def test_missing_name(self, mock_save):
        name = fake.name()
        position = fake.position()
        mock_employee = MagicMock()
        mock_employee.id = 1
        mock_employee.name = name
        mock_employee.position = position
        mock_save.return_value = mock_employee

        payload = {
            "name": name,
            "position": position
        }

        response = self.app.post('/employees/', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('name', response.json)

    def test_missing_position(self, mock_save):
        name = fake.name()
        position = fake.position()
        mock_employee = MagicMock()
        mock_employee.id = 1
        mock_employee.name = name
        mock_employee.position = position
        mock_save.return_value = mock_employee

        payload = {
            "name": name,
            "position": position
        }

        response = self.app.post('/employees/', json=payload)

        self.assertEqual(response.status_code, 400)
        self.assertIn('position', response.json)

