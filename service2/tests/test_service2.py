from flask import url_for
from flask_testing import TestCase
from app import app
from unittest.mock import patch

class TestBase(TestCase):
    def create_app(self):
        return app

class TestResponse(TestBase):
    def test_get_animal(self):

        for _ in range(1):
            response = self.client.post(url_for('get_animal'), json={"year": 1992, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Monkey"))
            response = self.client.post(url_for('get_animal'), json={"year": 1993, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Rooster"))
            response = self.client.post(url_for('get_animal'), json={"year": 1994, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Dog"))
            response = self.client.post(url_for('get_animal'), json={"year": 1995, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Pig"))
            response = self.client.post(url_for('get_animal'), json={"year": 1996, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Rat"))
            response = self.client.post(url_for('get_animal'), json={"year": 1997, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Ox"))
            response = self.client.post(url_for('get_animal'), json={"year": 1998, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Tiger"))
            response = self.client.post(url_for('get_animal'), json={"year": 1999, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Rabbit"))
            response = self.client.post(url_for('get_animal'), json={"year": 2000, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Dragon"))
            response = self.client.post(url_for('get_animal'), json={"year": 2001, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Snake"))
            response = self.client.post(url_for('get_animal'), json={"year": 2002, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Horse"))
            response = self.client.post(url_for('get_animal'), json={"year": 2003, "month": 4, "day":23})
            self.assertEqual(response.json['name'],("Sheep"))