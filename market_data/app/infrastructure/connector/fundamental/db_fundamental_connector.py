from dataclasses import asdict

from app.domain.model.fundamental import Fundamental
from app.domain.services.fundamental.connector import FundamentalConnector
from app.infrastructure.db import FundamentalEntry
from app.infrastructure.db.db_session import transaction_context


class FundamentalNotFoundException(Exception):
    pass


class DbFundamentalConnector(FundamentalConnector):
    def get_by_ticker_by_year(self, ticker: str, year: int) -> Fundamental:
        with transaction_context() as session:
            fundamental_entry: FundamentalEntry = session.query(FundamentalEntry).filter_by(ticker=ticker, year=year).first()
            if fundamental_entry is None:
                raise FundamentalNotFoundException(f'Fundamental not found for {ticker} {year}')
            fundamental = Fundamental(**{k: v for k, v in asdict(fundamental_entry).items() if k != 'id'})
        return fundamental

    def persist_fundamental(self, f: Fundamental):
        with transaction_context() as session:
            ent = FundamentalEntry(**asdict(f))
            session.add(ent)
