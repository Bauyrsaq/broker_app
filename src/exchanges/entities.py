from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Exchange(Base):
    __tablename__ = 'exchange'

    exchange_id = Column("exchange_id", String(3), primary_key=True)
    title = Column(String(128), nullable=False)
    country = Column(String(3), nullable=False)

    def __init__(self, title, exchange_id, country):
        self.title = title
        self.exchange_id = exchange_id
        self.country = country
    
    def __repr__(self):
        return f'<Exchange(title={self.title}, exchange_id={self.exchange_id}, country={self.country})>'