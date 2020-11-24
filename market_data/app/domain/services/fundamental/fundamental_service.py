from dataclasses import dataclass

from app.domain.model.fundamental import Fundamental
from app.domain.services.fundamental.connector import FundamentalConnector
from app.infrastructure.connector.fundamental.db_fundamental_connector import FundamentalNotFoundException


@dataclass
class FundamentalService:
    api_connector: FundamentalConnector
    db_connector: FundamentalConnector

    def get_by_ticker_by_year(self, ticker: str, year: int) -> Fundamental:
        try:
            f = self.db_connector.get_by_ticker_by_year(ticker, year)
        except FundamentalNotFoundException:
            f = self.api_connector.get_by_ticker_by_year(ticker, year)
        return f
