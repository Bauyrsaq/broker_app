from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Symbol(Base):
    __tablename__ = 'symbol'

    symbol_id = Column("symbol_id", String(3), primary_key=True)
    title = Column("title", String(128), nullable=False)
    ticker = Column("ticker", String(5), nullable=False)

    def __init__(self, symbol_id, title, ticker):
        self.title = title
        self.symbol_id = symbol_id
        self.ticker = ticker
    
    def __repr__(self):
        return f'Symbol(title={self.title}, symbol_id={self.symbol_id}, ticker={self.ticker})>'