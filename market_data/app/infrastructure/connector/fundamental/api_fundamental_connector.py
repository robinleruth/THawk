from app.domain.model.fundamental import Fundamental
from app.domain.services.fundamental.connector import FundamentalConnector


class ApiFundamentalConnector(FundamentalConnector):
    def get_by_ticker_by_year(self, ticker: str, year: int) -> Fundamental:
        pass

    def persist_fundamental(self, f: Fundamental):
        raise NotImplemented
