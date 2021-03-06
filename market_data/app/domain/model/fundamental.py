from dataclasses import dataclass, field


@dataclass
class Fundamental:
    ticker: str
    year: int
    market_cap: float = field(default_factory=float)
    debt_to_equity: float = field(default_factory=float)
    debt_to_asset: float = field(default_factory=float)
    revenue_per_share: float = field(default_factory=float)
    ni_per_share: float = field(default_factory=float)
    revenue: float = field(default_factory=float)
    gross_profit: float = field(default_factory=float)
    rd_expenses: float = field(default_factory=float)
    op_expenses: float = field(default_factory=float)
    op_income: float = field(default_factory=float)
    net_income: float = field(default_factory=float)
    cash: float = field(default_factory=float)
    cur_assets: float = field(default_factory=float)
    lt_assets: float = field(default_factory=float)
    total_assets: float = field(default_factory=float)
    cur_liab: float = field(default_factory=float)
    lt_debt: float = field(default_factory=float)
    lt_liab: float = field(default_factory=float)
    total_liab: float = field(default_factory=float)
    sh_equity: float = field(default_factory=float)
    cf_operations: float = field(default_factory=float)
    cf_investing: float = field(default_factory=float)
    cf_financing: float = field(default_factory=float)
    capex: float = field(default_factory=float)
    fcf: float = field(default_factory=float)
    dividends_paid: float = field(default_factory=float)
    gross_profit_margin: float = field(default_factory=float)
    op_margin: float = field(default_factory=float)
    int_coverage_: float = field(default_factory=float)
    net_profit_margin: float = field(default_factory=float)
    dividend_yield: float = field(default_factory=float)
    current_ratio: float = field(default_factory=float)
    operating_cycle: float = field(default_factory=float)
    days_of_ap_outstanding: float = field(default_factory=float)
    cash_conversion_cycle: float = field(default_factory=float)
    roa: float = field(default_factory=float)
    roe: float = field(default_factory=float)
    roce: float = field(default_factory=float)
    price_earning_ratio: float = field(default_factory=float)
    price_to_sale_ratio: float = field(default_factory=float)
    price_to_book_ratio: float = field(default_factory=float)
    price_to_free_cash_flow: float = field(default_factory=float)
    price_earning_to_growth_ratio: float = field(default_factory=float)
    earning_per_share: float = field(default_factory=float)
