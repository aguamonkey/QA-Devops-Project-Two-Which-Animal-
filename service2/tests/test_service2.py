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
            response = self.client.post(url_for('get_animal'), json={"year": 1992, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Monkey"))