from sqlalchemy import Column, Float, Integer, String, Boolean
import numpy as np
import pandas as pd
from persistance.db_connection.db_connector import Base

def create_db_class(class_name : str, df):
    class_name = class_name.replace(' ', '_')
    attributes = create_attributes_dict(class_name, df)
    new_class = type(class_name, (Base,), attributes)
    return new_class

def create_attributes_dict(class_name : str, df):
    attributes = {
        '__tablename__': class_name.lower(),
        'id': Column(Integer, primary_key=True)
    }

    for col_name in df.columns:
        attribute_name = col_name
        attribute_type = None
        col_type = df[col_name].dtype
        if col_type == 'float64' or col_type == 'float32' or col_type == 'int64' or col_type == 'int8':
            attribute_type = Column(Float)
        elif col_type == 'object':
            attribute_type = Column(String)
        elif col_type == 'bool':
            attribute_type = Column(Boolean)
        else:
            print('unknown/unusable data type: {}'.format(col_type))
            continue
        attributes[attribute_name] = attribute_type
    return attributes

'''
Sources:
https://docs.scipy.org/doc/numpy/reference/generated/numpy.dtype.kind.html
'''