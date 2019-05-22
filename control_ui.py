import inner_wear.transfer as tf
import persistance.db_operator as db_operator
from inner_wear.db_model.Cloth import Cloth
import visualization.visualizer as vis
import inner_wear.custom_cleaning as c_cleaning
import sys

# TODO: Replace/supplement with terminal commands

def add_data_set():
    csv_path = input('path to csv file: ')
    tf.transfer_csv_cloth_to_db(csv_path, 'DB_INNERWEAR_ORG')
    print('The file ' + csv_path + 'was added to database DB_INNERWEAR_ORG')
    start()

def show_bar_chart_summary():
    db_name = input('DB config section: ')
    cloths = db_operator.db_get_all_entrys_of(db_name, Cloth)
    vis.bar_chart_summary(cloths)
    start()

def transfer_db_to_db():
    source_db = input('source db: ')
    target_db = input('target db: ')
    tf.transfer_from_db1_to_db2(source_db, target_db)
    start()

def manual_data_unification():
    source_db = input('source db: ')
    search_column = input('column: ')
    search_query = input('sub string searched for: ')
    replacment_string = input('replacment string: ')
    c_cleaning.clean_column_string_values(source_db, Cloth, search_column, search_query, replacment_string)
    start()

###############################################
#           start of program                  #
###############################################
def start():
    command = input('\n\ncommand: ')

    if command == 'exit':
       sys.exit()

    ###############
    # db operations
    ###############
    if command == 'add_data_set':
        add_data_set()
    if command == 'db_transfer':
        transfer_db_to_db()
    if command == 'm_data_uni':
        manual_data_unification()

    ###############
    # visualization
    ###############
    if command == 'vis_attr_sum':
        show_bar_chart_summary()

    start()
start()