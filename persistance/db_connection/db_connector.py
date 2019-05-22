from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

from persistance.db_connection.config_loader import config


def db_connect(db_config_section):
    """ Connect to the PostgreSQL database server """
    #try:
    # read connection parameters
    postgres_params = config(db_config_section)
    print('connecting to: ', postgres_params['connection_url_default'])
    postgres_engine = create_engine(postgres_params['connection_url_default'])
    print('connected')
    return postgres_engine
    # except:
    #    print("db connection failed")
    #    sys.exit(1)

# Base
Base = declarative_base()



