# project/tests/test_users/py
import unittest
from project.tests.base import BaseTestCase
from flask import json


class TestUserService(BaseTestCase):
    """Tests for user controller"""

    def test_users(self):
        response = self.client.get('/users')
        self.assertEqual(response.status_code, 200)

    def test_add_user(self):
        with self.client:
            response = self.client.post(
                '/users/add',
                data=json.dumps(dict(
                    username='luis',
                    email='luis@testinggg.com'
                )),
                content_type='application/json',
            )

            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 200)
            self.assertEqual(data['username'], 'luis')
            self.assertEqual(data['email'], 'luis@testinggg.com')

    def test_add_user_invalid_json(self):
        """Ensure error is thrown if the JSON object is empty."""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict()),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_invalid_json_keys(self):
        """Ensure error is thrown if the JSON object does not have a username key."""
        with self.client:
            response = self.client.post(
                '/users',
                data=json.dumps(dict(email='michael@realpython.com')),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertIn('Invalid payload.', data['message'])
            self.assertIn('fail', data['status'])

    def test_add_user_duplicate_user(self):
        """Ensure error is thrown if the email already exists."""
        with self.client:
            self.client.post(
                '/users',
                data=json.dumps(dict(
                    username='michael',
                    email='mischael@realpython.com'
                )),
                content_type='application/json',
            )
            response = self.client.post(
                '/users',
                data=json.dumps(dict(
                    username='michael2',
                    email='michael@realpython.com'
                )),
                content_type='application/json',
            )
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 500)
            self.assertIn('Email Already Exists.', data['message'])
            self.assertIn('fail', data['status'])



if __name__ == '__main__':
    unittest.main()
