from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker

from persistance.db_connection.db_connector import Base
from persistance.db_connection.db_connector import db_connect
from sqlalchemy import Table
import pandas as pd

INNERWEAR_ORG = "DB_INNERWEAR_ORG"

def db_save(objects:[], db_config_section:str):
    session, engine = _create_session(db_config_section)
    for obj in objects:
        session.add(obj)
    session.flush()
    session.commit()
    session.close()

def db_get_all_entrys_of(db_config_section:str, table_name):
    session, engine = _create_session(db_config_section)
    new_class = _create_class_by_table(table_name, engine)
    objects = session.query(new_class).all()
    session.close()
    return objects

def db_get_by_id(obj_id, db_config_section:str, table_name):
    session, engine = _create_session(db_config_section)
    new_class = _create_class_by_table(table_name, engine)
    obj = session.query(new_class).get(obj_id)
    return obj

def clone_table_from_db_to_db(db_config_section_source, db_config_section_target, table_names=['cloth']):
    session_source, engine_source = _create_session(db_config_section_source)
    session_target, engine_target = _create_session(db_config_section_target)
    meta_source = MetaData(bind=engine_source)
    meta_source.reflect(bind=engine_source)

    for table_name in table_names:
        print('cloning table ' + table_name)
        table = meta_source.tables[table_name]
        table.create(engine_target, checkfirst=True)
        data = session_source.execute(table.select()).fetchall()
        print('inserting data to target db')
        if data:
            print(table.insert())
            engine_target.execute(table.insert(), data)

def db_table_to_pandas_data_frame(db_config_section:str, table_name: str):
    session, engine = _create_session(db_config_section)
    df = pd.read_sql_table(table_name, engine)
    return df


##############################################################
def _create_class_by_table(table_name, engine):
    table = Table(table_name, Base.metadata, autoload=True, autoload_with=engine)
    class_name = table_name.capitalize()
    attributes = {'__table__': table}
    new_class = type(class_name, (Base,), attributes)
    return new_class

def _create_session(db_config_section:str):
    # CONNECT TO DB
    # create an engine
    engine = db_connect(db_config_section)
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    return session, engine
