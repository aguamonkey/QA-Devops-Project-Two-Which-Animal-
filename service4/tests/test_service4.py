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
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Rooster", luck_number = 55),
            )
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Dog", luck_number = 55),
            )
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Pig", luck_number = 55),
            )
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Rat", luck_number = 55),
            )
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Ox", luck_number = 55),
            )
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Tiger", luck_number = 55),
            )
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Dragon", luck_number = 55),
            )
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Rabbit", luck_number = 55),
            )
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Horse", luck_number = 55),
            )
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Snake", luck_number = 55),
            )
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Sheep", luck_number = 55),
            )
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)

            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Monkey", luck_number = 77),
            )
            self.assertIn(b'This is going to be a great year in which all of your dreams come true', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Rooster", luck_number = 77),
            )
            self.assertIn(b'This is going to be a great year in which all of your dreams come true', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Dog", luck_number = 77),
            )
            self.assertIn(b'This is going to be a great year in which all of your dreams come true', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Pig", luck_number = 77),
            )
            self.assertIn(b'This is going to be a great year in which all of your dreams come true', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Rat", luck_number = 77),
            )
            self.assertIn(b'This is going to be a great year in which all of your dreams come true', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Ox", luck_number = 77),
            )
            self.assertIn(b'This is going to be a great year in which all of your dreams come true', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Tiger", luck_number = 77),
            )
            self.assertIn(b'This is going to be a great year in which all of your dreams come true', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Dragon", luck_number = 77),
            )
            self.assertIn(b'This is going to be a great year in which all of your dreams come true', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Rabbit", luck_number = 77),
            )
            self.assertIn(b'This is going to be a great year in which all of your dreams come true', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Horse", luck_number = 77),
            )
            self.assertIn(b'This is going to be a great year in which all of your dreams come true', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Snake", luck_number = 77),
            )
            self.assertIn(b'This is going to be a great year in which all of your dreams come true', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Sheep", luck_number = 77),
            )
            self.assertIn(b'This is going to be a great year in which all of your dreams come true', response.data)
            
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Monkey", luck_number = 22),
            )
            self.assertIn(b'This will be a hard year but will make you stronger', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Rooster", luck_number = 22),
            )
            self.assertIn(b'This will be a hard year but will make you stronger', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Dog", luck_number = 22),
            )
            self.assertIn(b'This will be a hard year but will make you stronger', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Pig", luck_number = 22),
            )
            self.assertIn(b'This will be a hard year but will make you stronger', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Rat", luck_number = 22),
            )
            self.assertIn(b'This will be a hard year but will make you stronger', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Ox", luck_number = 22),
            )
            self.assertIn(b'This will be a hard year but will make you stronger', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Tiger", luck_number = 22),
            )
            self.assertIn(b'This will be a hard year but will make you stronger', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Dragon", luck_number = 22),
            )
            self.assertIn(b'This will be a hard year but will make you stronger', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Rabbit", luck_number = 22),
            )
            self.assertIn(b'This will be a hard year but will make you stronger', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Horse", luck_number = 22),
            )
            self.assertIn(b'This will be a hard year but will make you stronger', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Snake", luck_number = 22),
            )
            self.assertIn(b'This will be a hard year but will make you stronger', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Sheep", luck_number = 22),
            )
            self.assertIn(b'This will be a hard year but will make you stronger', response.data)
            