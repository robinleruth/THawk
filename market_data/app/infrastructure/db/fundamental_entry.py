from dataclasses import dataclass

from sqlalchemy import Column, Integer, String, Float

from app.infrastructure.db import Base


@dataclass
class FundamentalEntry(Base):
    __tablename__ = 't_marketdata_fundamental'

    id: int = Column(Integer, primary_key=True)
    ticker: str = Column(String)
    year: int = Column(Integer)
    market_cap: float = Column(Float)
    debt_to_equity: float = Column(Float)
    debt_to_asset: float = Column(Float)
    revenue_per_share: float = Column(Float)
    ni_per_share: float = Column(Float)
    revenue: float = Column(Float)
    gross_profit: float = Column(Float)
    rd_expenses: float = Column(Float)
    op_expenses: float = Column(Float)
    op_income: float = Column(Float)
    net_income: float = Column(Float)
    cash: float = Column(Float)
    cur_assets: float = Column(Float)
    lt_assets: float = Column(Float)
    total_assets: float = Column(Float)
    cur_liab: float = Column(Float)
    lt_debt: float = Column(Float)
    lt_liab: float = Column(Float)
    total_liab: float = Column(Float)
    sh_equity: float = Column(Float)
    cf_operations: float = Column(Float)
    cf_investing: float = Column(Float)
    cf_financing: float = Column(Float)
    capex: float = Column(Float)
    fcf: float = Column(Float)
    dividends_paid: float = Column(Float)
    gross_profit_margin: float = Column(Float)
    op_margin: float = Column(Float)
    int_coverage_: float = Column(Float)
    net_profit_margin: float = Column(Float)
    dividend_yield: float = Column(Float)
    current_ratio: float = Column(Float)
    operating_cycle: float = Column(Float)
    days_of_ap_outstanding: float = Column(Float)
    cash_conversion_cycle: float = Column(Float)
    roa: float = Column(Float)
    roe: float = Column(Float)
    roce: float = Column(Float)
    price_earning_ratio: float = Column(Float)
    price_to_sale_ratio: float = Column(Float)
    price_to_book_ratio: float = Column(Float)
    price_to_free_cash_flow: float = Column(Float)
    price_earning_to_growth_ratio: float = Column(Float)
    earning_per_share: float = Column(Float)
