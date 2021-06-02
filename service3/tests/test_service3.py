from flask import url_for
from flask_testing import TestCase

from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_number(self):

        for _ in range(20):
            response = self.client.get(url_for('get_number'))
            self.assertIn(response.json['luck_number'], range(0,100))