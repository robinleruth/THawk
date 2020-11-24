import abc

from app.domain.model.fundamental import Fundamental


class FundamentalConnector(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_by_ticker_by_year(self, ticker: str, year: int) -> Fundamental:
        pass

    @abc.abstractmethod
    def persist_fundamental(self, f: Fundamental):
        pass

