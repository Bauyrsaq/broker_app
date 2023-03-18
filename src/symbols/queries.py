from sqlalchemy import select

from symbols.entities import Symbol


class GetSymbolByIdQuery():
    def __init__(self, db_session):
        self.db_session = db_session

    def execute(self, symbol_id: str):
        query = select(Symbol).where(Symbol.symbol_id == symbol_id)

        symbol = self.db_session.execute(query)

        return symbol