import pandas as pd
import db_model.db_model_factory as db_factory
import inspect

import persistance.db_operator as db_op
from db_model.inner_wear.Cloth import Cloth


def transfer_csv_cloth_to_db(csv_path, db_config_section):
    cloth_products = []
    df = pd.read_csv(csv_path, header=0)
    df = df.fillna('Nan')

    for df_obj in df.iterrows():
        product_name = str(df_obj[1][0])
        mrp = df_obj[1][1]
        price = df_obj[1][2]
        pdp_url = df_obj[1][3]
        brand_name = df_obj[1][4]
        product_category = df_obj[1][5]
        retailer = df_obj[1][6]
        description = df_obj[1][7]
        style_attributes = df_obj[1][10]
        total_size = df_obj[1][11]
        available_size = df_obj[1][12]
        color = df_obj[1][13]

        if df_obj[1][8] == 'Nan':
            rating = '0'
        else:
            rating = df_obj[1][8]
        if df_obj[1][9] == 'Nan':
            review_count = '0'
        else:
            review_count = df_obj[1][9]

        cloth_obj = Cloth(product_name, mrp, price, pdp_url, brand_name, product_category, retailer, description, rating, review_count, style_attributes, total_size, available_size, color)
        cloth_products.append(cloth_obj)

    db_op.db_save(cloth_products, db_config_section)
    print('done')

def transfer_csv_to_db(csv_path, table_name, db_config_section):
    objects = []
    df = pd.read_csv(csv_path, header=0)
    df.columns = df.columns.str.replace(' ', '_')  # incase column names contain a space they are replaced with _
    df.columns = map(str.lower, df.columns)  # all column names to lower case
    df = df.fillna('Nan')

    NewClass = db_factory.create_db_class(table_name, df)  # creates class out of data frame column names and the table name
    print(type(NewClass()))
    attributes = inspect.getmembers(NewClass, lambda a: not (inspect.isroutine(a)))  # gets all attribute names  off class
    attributes = [a[0] for a in attributes if not(a[0].startswith('__') and a[0].endswith('__')) and a[0] != 'id']  # filters out attribute names beginning and ending with '__' or id attribute

    print('attributes: {}'.format(attributes))
    for df_obj in df.iterrows():
         new_class_obj = NewClass()
         for attribute in attributes:
             setattr(new_class_obj, attribute, df_obj[attribute])


    db_op.db_save(objects, db_config_section)
    print('done')
    print('created class/table {}'.format(type(NewClass)))


def transfer_from_db1_to_db2(db_config_section_source, db_config_section_target):
    db_op.clone_table_from_db_to_db(db_config_section_source, db_config_section_target)