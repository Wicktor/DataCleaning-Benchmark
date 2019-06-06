from sqlalchemy import Column, Float, Integer, String, Boolean
from persistance.db_connection.db_connector import Base

def create_db_class(class_name : str, df):
    '''
    This function will create dynamically a class/database-model that fits the given pandas data frame 
    :param class_name: name of the class that also can mirror the table name later on
    :param df: pandas data frame that contains the data 
    :return: 
    '''
    class_name = class_name.replace(' ', '_')  # replace spaces to prevent errors and unify names
    attributes = create_attributes_dict(class_name, df)
    new_class = type(class_name, (Base,), attributes)  # this command finally creates the model
    return new_class

def create_attributes_dict(class_name : str, df):
    '''
    This function converts column names to class properties/attributes
    :param class_name: name of the class that also mirrors the table name
    :param df: pandas data frame that contains the data
    :return: 
    '''
    attributes = {
        '__tablename__': class_name.lower(),
        'id': Column(Integer, primary_key=True)
    }

    for col_name in df.columns:
        attribute_name = col_name  # the attribute is named after the column name
        attribute_type = None
        col_type = df[col_name].dtype  # get the kind of data that is saved in the column
        if col_type == 'float64' or col_type == 'float32' or col_type == 'int64' or col_type == 'int8':
            attribute_type = Column(Float)
        elif col_type == 'object':
            attribute_type = Column(String)  # TODO: here a distinction between a string and a list/array is missing.
        elif col_type == 'bool':
            attribute_type = Column(Boolean)
        else:  # skip column if the type is unknown for some reason
            print('unknown/unusable data type: {}'.format(col_type))
            continue
        attributes[attribute_name] = attribute_type
    return attributes

'''
Sources:
https://docs.scipy.org/doc/numpy/reference/generated/numpy.dtype.kind.html
'''