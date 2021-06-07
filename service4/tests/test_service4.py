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
                json=dict(name = "Happy Pigeon", luck_number = 5),
            )
            self.assertIn(b'You will have to be moderate in your seed consumption', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Sad Pigeon", luck_number = 5),
            )
            self.assertIn(b'You will have to be moderate in your seed consumption', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Angry Pigeon", luck_number = 5),
            )
            self.assertIn(b'You will have to be moderate in your seed consumption', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Excited Pigeon", luck_number = 5),
            )
            self.assertIn(b'You will have to be moderate in your seed consumption', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Depressed Pigeon", luck_number = 5),
            )
            self.assertIn(b'You will have to be moderate in your seed consumption', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Anxious Pigeon", luck_number = 5),
            )
            self.assertIn(b'You will have to be moderate in your seed consumption', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Fierce Pigeon", luck_number = 5),
            )
            self.assertIn(b'You will have to be moderate in your seed consumption', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Grumpy Pigeon", luck_number = 5),
            )
            self.assertIn(b'You will have to be moderate in your seed consumption', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Sleepy Pigeon", luck_number = 5),
            )
            self.assertIn(b'You will have to be moderate in your seed consumption', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Beautiful Pigeon", luck_number = 5),
            )
            self.assertIn(b'You will have to be moderate in your seed consumption', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Evil Pigeon", luck_number = 5),
            )
            self.assertIn(b'You will have to be moderate in your seed consumption', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Hero Pigeon", luck_number = 5),
            )
            self.assertIn(b'You will have to be moderate in your seed consumption', response.data)

            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Happy Pigeon", luck_number = 7),
            )
            self.assertIn(b'You will get all the seeds you desire this year', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Sad Pigeon", luck_number = 7),
            )
            self.assertIn(b'You will get all the seeds you desire this year', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Angry Pigeon", luck_number = 7),
            )
            self.assertIn(b'You will get all the seeds you desire this year', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Excited Pigeon", luck_number = 7),
            )
            self.assertIn(b'You will get all the seeds you desire this year', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Depressed Pigeon", luck_number = 7),
            )
            self.assertIn(b'You will get all the seeds you desire this year', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Anxious Pigeon", luck_number = 7),
            )
            self.assertIn(b'You will get all the seeds you desire this year', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Fierce Pigeon", luck_number = 7),
            )
            self.assertIn(b'You will get all the seeds you desire this year', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Grumpy Pigeon", luck_number = 7),
            )
            self.assertIn(b'You will get all the seeds you desire this year', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Sleepy Pigeon", luck_number = 7),
            )
            self.assertIn(b'You will get all the seeds you desire this year', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Beautiful Pigeon", luck_number = 7),
            )
            self.assertIn(b'You will get all the seeds you desire this year', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Evil Pigeon", luck_number = 7),
            )
            self.assertIn(b'You will get all the seeds you desire this year', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Hero Pigeon", luck_number = 7),
            )
            self.assertIn(b'You will get all the seeds you desire this year', response.data)
            
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Happy Pigeon", luck_number = 2),
            )
            self.assertIn(b'You will go hungry', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Sad Pigeon", luck_number = 2),
            )
            self.assertIn(b'You will go hungry', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Angry Pigeon", luck_number = 2),
            )
            self.assertIn(b'You will go hungry', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Excited Pigeon", luck_number = 2),
            )
            self.assertIn(b'You will go hungry', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Depressed Pigeon", luck_number = 2),
            )
            self.assertIn(b'You will go hungry', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Anxious Pigeon", luck_number = 2),
            )
            self.assertIn(b'You will go hungry', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Fierce Pigeon", luck_number = 2),
            )
            self.assertIn(b'You will go hungry', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Grumpy Pigeon", luck_number = 2),
            )
            self.assertIn(b'You will go hungry', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Sleepy Pigeon", luck_number = 2),
            )
            self.assertIn(b'You will go hungry', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Beautiful Pigeon", luck_number = 2),
            )
            self.assertIn(b'You will go hungry', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Evil Pigeon", luck_number = 2),
            )
            self.assertIn(b'You will go hungry', response.data)
            response = self.client.post(
                url_for('get_fortune'),
                json=dict(name = "Hero Pigeon", luck_number = 2),
            )
            self.assertIn(b'You will go hungry', response.data)
            