import pandas as pd
from inner_wear.db_model.Cloth import Cloth
import persistance.db_operator as db_op
import persistance.db_model_factory as m_fac

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

def transfer_csv__to_db(csv_path, db_config_section):
    objects = []
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


def transfer_from_db1_to_db2(db_config_section_source, db_config_section_target):
    db_op.clone_table_from_db_to_db(db_config_section_source, db_config_section_target)