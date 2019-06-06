from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker

from persistance.db_connection.db_connector import Base
from persistance.db_connection.db_connector import db_connect
from sqlalchemy import Table
import pandas as pd
import db_model.db_model_factory as db_factory
import inspect



def db_save(objects:[], db_config_section:str):
    session, engine = _create_session(db_config_section)
    for obj in objects:
        session.add(obj)
    session.flush()
    session.commit()
    session.close()

def db_get_all_entrys_of_table(db_config_section:str, table_name):
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

def clone_tables_from_sdb_to_tdb(db_config_section_source, db_config_section_target, table_names):
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
##############################################################
def transfer_df_to_db(df, table_name, db_config_section):
    objects = []
    NewClass = db_factory.create_db_class(table_name, df)  # creates class out of data frame column names and the table name
    attributes = inspect.getmembers(NewClass, lambda a: not (inspect.isroutine(a)))  # gets all attribute names  off class
    attributes = [a[0] for a in attributes if not (a[0].startswith('__') and a[0].endswith('__')) and a[
        0] != 'id']  # filters out attribute names beginning and ending with '__' or id attribute

    # print('attributes: {}'.format(attributes))
    for df_obj in df.iterrows():
        new_class_obj = NewClass()
        for attribute in attributes:
            setattr(new_class_obj, attribute, df_obj[attribute])

    db_save(objects, db_config_section)
    # print('done')
    print('created class/table {}'.format(type(NewClass)))


def transfer_csv_to_db(csv_path, table_name, db_config_section):
    df = pd.read_csv(csv_path, header=0)
    df.columns = df.columns.str.replace(' ', '_')  # incase column names contain a space they are replaced with _
    df.columns = map(str.lower, df.columns)  # all column names to lower case
    df = df.fillna('Nan')
    transfer_df_to_db(df, table_name, db_config_section)



##############################################################
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
    session = Session()

    return session, engine
