import unittest
from flask import Flask
from flask_testing import TestCase
from app import app

class FlaskAppTests(TestCase):
    def test_start_form(self):
        with app.test_client() as client:
            resp = client.get('/')
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h1>Currency Converter</h1>', html)


def test_form_submit(self):
    with app.test_client() as client:
        resp = client.post(
            '/complete', data={'confrom': 'USD', 'conto': 'USD', 'amount': '1.0'})
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('The results are: $ 1.0', html)

def test_blank_entry(self):
    with app.test_client() as client:
        resp = client.post('/complete', data={'confrom:', 'conto': 'USD', 'amount': '1.0'})
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('<h1> Please fill in all fields!</h1>', html)

def test_incorrect_code(self):
    with app.test_client() as client:
        resp = client.post(
            '/complete', data={'confrom': 'ZZZ', 'conto': 'USD', 'amount': '1.0'})
        html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn('<h1> You have entered an invalid "from" property. [Example: from=EUR]</h1>', html)

