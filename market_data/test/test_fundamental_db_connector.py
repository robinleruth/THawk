import os

os.environ['APP_ENV'] = 'test'
import unittest
from app.domain.model.fundamental import Fundamental

from app.infrastructure.connector.fundamental.db_fundamental_connector import DbFundamentalConnector, \
    FundamentalNotFoundException
from app.infrastructure.db import engine, Base, FundamentalEntry
from app.infrastructure.db.db_session import transaction_context


class TestFundamentalDbConnector(unittest.TestCase):
    def setUp(self) -> None:
        Base.metadata.create_all(bind=engine)
        self.connector = DbFundamentalConnector()
        ent = FundamentalEntry(ticker='AAPL', year=2010)
        with transaction_context() as session:
            session.add(ent)

    def tearDown(self) -> None:
        Base.metadata.drop_all(bind=engine)

    def test_get_by_ticker_by_year(self):
        fundamental = self.connector.get_by_ticker_by_year('AAPL', 2010)
        self.assertTrue(fundamental is not None)
        self.assertEqual(2010, fundamental.year)
        self.assertEqual('AAPL', fundamental.ticker)

    def test_not_found_exception(self):
        self.assertRaises(FundamentalNotFoundException, self.connector.get_by_ticker_by_year, 'GOOG', 2010)

    def test_persist_entry(self):
        f = Fundamental(ticker='GOOG', year=2010)
        self.connector.persist_fundamental(f)
        with transaction_context() as session:
            lst = session.query(FundamentalEntry).all()
            self.assertEqual(2, len(lst))
