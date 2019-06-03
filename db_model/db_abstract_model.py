from persistance.db_connection.db_connector import Base
from sqlalchemy import Table

class AbstractModel(Base):
    __table__ = None
    def __init__(self, table_name, engine):
        self.__table__ = Table('mytable', Base.metadata,
                          autoload=True, autoload_with=engine)