from flask import url_for
from flask_testing import TestCase
import requests_mock
from app import app
import datetime
import os

class TestBase(TestCase):
    def create_app(self):

        SECRET_KEY = os.urandom(32)

        # Pass in testing configurations for the app. Here we use sqlite without a persistent database for our tests.
        app.config.update(SQLALCHEMY_DATABASE_URI='sqlite:///test.db',
                SECRET_KEY=SECRET_KEY,
                DEBUG=True,
                WTF_CSRF_ENABLED=False
                )
        return app
class TestHome(TestBase):
    def test_home(self):
        with requests_mock.Mocker() as mocker:
            mocker.post('http://which_animal_am_i_name_api:5000/get_animal', json={'name' : 'Happy Pigeon'})
            mocker.get('http://which_animal_am_i_luck_api:5000/get_number', json={'luck_number' : 55})
            mocker.post('http://which_animal_am_i_fortune_api:5000/get_fortune', text='This is going to be a year of ups and downs but in the end it will be a good one')

            response = self.client.post(url_for('home'),data={"birthdate" : datetime.date(1992, 4, 23)})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Happy Pigeon', response.data)
            self.assertIn(b'55', response.data)
            self.assertIn(b'This is going to be a year of ups and downs but in the end it will be a good one', response.data)
