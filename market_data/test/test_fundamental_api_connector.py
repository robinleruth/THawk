import os

os.environ['APP_ENV'] = 'test'
import unittest

from app.infrastructure.connector.fundamental.api_fundamental_connector import ApiFundamentalConnector


class TestFundamentalApiConnector(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.connector = ApiFundamentalConnector()

    def test_persist(self):
        self.assertRaises(NotImplementedError, self.connector.persist_fundamental, None)
