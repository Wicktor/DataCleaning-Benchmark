import sys
# import holoclean  # TODO: holoclean installation bugged, path can not be set
# from detect import NullDetector, ViolationDetector
# from repair.featurize import *
import persistance.db_operator as db_op

bd_config_section = 'DB_INNERWEAR_V1_ORG'
table_name = 'cloth'
df = db_op.db_table_to_pandas_data_frame(bd_config_section, table_name, ['brand_name'], 'brand_name_corrected')


def holoclean_benchmark_test(bd_config_section, table_name, source_columns, target_column_name, num_epochs=100):
    df = db_op.db_table_to_pandas_data_frame(bd_config_section, table_name)
    

