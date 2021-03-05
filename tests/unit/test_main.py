import unittest
import tests.facades as users_facade

from handlers.main import handler


class TestMainFunction(unittest.TestCase):

    def setUp(self):
        users_facade.create_user(1, "Rafael")

    def test_should_return_username(self):
        event = {"user_id": 1}
        expected = {'body': '{"username": "Rafael"}', 'statusCode': 200}

        actual = handler(event, None)

        self.assertEqual(actual, expected)

    def test_should_return_user_does_not_exist(self):
        event = {"user_id": 2}
        expected = {'statusCode': 500, 'body': 'User does not exist'}

        actual = handler(event, None)

        self.assertEqual(actual, expected)

    def tearDown(self):
        users_facade.reset_database()
