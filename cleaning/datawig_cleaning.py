import datawig
import pandas as pd
import persistance.db_operator as db_op

# bd_config_section = 'DB_INNERWEAR_V1_ORG'
# table_name = 'cloth'
# df = db_op.db_table_to_pandas_data_frame(bd_config_section, table_name)


def datawig_benchmark_test(bd_config_section, table_name, source_columns, target_column, num_epochs=100):
    df = db_op.db_table_to_pandas_data_frame(bd_config_section, table_name)
    df_train, df_test = datawig.utils.random_split(df)

    imputer = imputer_v1() # TODO: sould be dynamic depending on call/comand or so

    # Fit an imputer model on the train data
    imputer.fit(train_df=df_train, num_epochs=num_epochs)
    # Impute missing values and return original dataframe with predictions
    df_corrected = imputer.predict(df_test)

    db_op.



################################################################
#                     imputer models                           #
################################################################
def imputer_v1():
    imputer = datawig.SimpleImputer(
        input_columns=['brand_name'],  # column(s) containing information about the column we want to impute
        output_column='label',  # the column we'd like to impute values for
        output_path='imputer_model'  # stores model data and metrics
    )
    return imputer