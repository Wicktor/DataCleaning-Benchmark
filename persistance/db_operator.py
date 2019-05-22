from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker

from persistance.db_connection.db_connector import Base
from persistance.db_connection.db_connector import db_connect

INNERWEAR_ORG = "DB_INNERWEAR_ORG"

def create_session(db_config_section:str):
    # CONNECT TO DB
    # create an engine
    engine = db_connect(db_config_section)
    Base.metadata.create_all(engine)

    # create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # create a Session
    session = Session()

    return session, engine

def db_save(objects:[], db_config_section:str):
    session, engine = create_session(db_config_section)
    for obj in objects:
        session.add(obj)
    session.flush()
    session.commit()
    session.close()

def db_get_all_entrys_of(db_config_section:str, class_type):  # TODO: rename class_type to table_name
    session, engine = create_session(db_config_section)
    objects = session.query(class_type).all()
    session.close()
    return objects

def db_get_by_id(obj_id, db_config_section:str, class_type):  # TODO: rename class_type to table_name
    session, engine = create_session(db_config_section)
    obj = session.query(class_type).get(obj_id)
    session.flush()
    session.commit()
    session.close()
    return obj

# def db_get_by_properties(properties:[], db_config_section:str, table_name):
#     print('NOT IMPLEMENRED')
#     return None
#     session, engine = create_session(db_config_section)
#
#     session.flush()
#     session.commit()
#     session.close()
#     return None

def clone_table_from_db_to_db(db_config_section_source, db_config_section_target, table_names=['cloth']):
    session_source, engine_source = create_session(db_config_section_source)
    session_target, engine_target = create_session(db_config_section_target)
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