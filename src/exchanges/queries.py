from sqlalchemy import select

from exchanges.entities import  Exchange


class GetExchangeByIdQuery():
    def __init__(self, db_session):
        self.db_session = db_session
    
    def execute(self, exchange_id: str):
        query = select(Exchange).where(Exchange.exchange_id == exchange_id)

        exchange = self.db_session.execute(query)

        return exchange
