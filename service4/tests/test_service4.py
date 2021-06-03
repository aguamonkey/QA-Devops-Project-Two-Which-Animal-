from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_animal(self):
    
        for _ in range(20):
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Monkey", luck_number = 55),
            )
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)