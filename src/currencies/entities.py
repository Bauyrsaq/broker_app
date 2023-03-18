from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Currency(Base):
    __tablename__ = 'currency'

    currency_id = Column("currency_id", String(3), primary_key=True)
    title = Column(String(128), nullable=False)
    symbol = Column(String(5), nullable=True)

    def __init__(self, title, currency_id, symbol):
        self.title = title
        self.currency_id = currency_id
        self.symbol = symbol

    def __repr__(self):
        return f'<Currency(title={self.title}, currency_id={self.currency_id}, symbol={self.symbol})>'
