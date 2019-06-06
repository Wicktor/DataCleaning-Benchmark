import sys
# import cleaning.custom_cleaning as c_cleaning
import persistance.db_operator as db_operator
import visualization.visualizer as vis
# TODO: Replace/supplement with terminal commands

def add_data_set():
    csv_path = input('path to csv file: ')
    target_database = input('target db config section: ')
    db_operator.transfer_csv_to_db(csv_path, target_database)
    print('The file ' + csv_path + 'was added to database DB_INNERWEAR_ORG')
    start()

def show_bar_chart_summary():
    db_section = input('DB config section: ')
    table_name = input('Name of the table: ')
    instances = db_operator.db_get_all_entrys_of_table(db_section, table_name)
    vis.bar_chart_summary(instances)
    start()

def transfer_db_to_db():
    source_db = input('source db: ')
    target_db = input('target db: ')
    db_operator.clone_tables_from_sdb_to_tdb(source_db, target_db)
    start()

# def manual_data_unification():
#     source_db = input('source db: ')
#     search_column = input('column: ')
#     search_query = input('sub string searched for: ')
#     replacment_string = input('replacment string: ')
#     c_cleaning.clean_column_string_values(source_db, Cloth, search_column, search_query, replacment_string)
#     start()



###############################################
#           start of program                  #
###############################################
# TODO: Replace/supplement with terminal commands
def start():
    '''
    Recursive function to create small rough text based ui 
    '''
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
    # if command == 'm_data_uni':
    #     manual_data_unification()

    ###############
    # visualization
    ###############
    if command == 'vis_attr_sum':
        show_bar_chart_summary()

    start()

start()

