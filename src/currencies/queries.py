from sqlalchemy import select

from currencies.entities import Currency


class GetCurrencyByIdQuery():
    def __init__(self, db_session):
        self.db_session = db_session

    def execute(self, currency_id: str):
        query = select(Currency).where(Currency.currency_id == currency_id)

        currency = self.db_session.execute(query)

        return currency
