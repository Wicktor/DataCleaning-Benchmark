import datawig
import persistance.db_operator as db_op

def datawig_benchmark_test(bd_config_section, table_name, source_columns, target_column_name, num_epochs=100):
    df = db_op.db_table_to_pandas_data_frame(bd_config_section, table_name)
    # df[target_column_name] = 'test'  # adding empty column that will be filled with the corrected values
    print('data frame created out of db.')
    print(df.iloc[0])
    # TODO: start time
    # TODO: loop
    df_train, df_test = datawig.utils.random_split(df)

    imputer = imputer_v1(source_columns, target_column_name) # TODO: sould be dynamic depending on call/command or so
    print('inputer created')
    # Fit an imputer model on the train data
    imputer.fit(train_df=df_train, num_epochs=num_epochs)
    print('fitting done')
    # Impute missing values and return original dataframe with predictions
    df_corrected = imputer.predict(df_test)
    print('correction done')
    print('###########\n\n###########')
    # TODO: end time --> total time
    # TODO: after loop median calculation, save results

    print(df.iloc[0])
    print('writing result to db')
    new_table_name = table_name + '_corrected'
    db_op.transfer_df_to_db(df_corrected, new_table_name, bd_config_section)
    print('done')  # TODO: delete this



################################################################
#                     imputer models                           #
################################################################
def imputer_v1(source_columns, target_column_name):
    imputer = datawig.SimpleImputer(
        input_columns=source_columns,  # column(s) containing information about the column we want to impute
        output_column=target_column_name,  # the column we'd like to impute values for
        output_path='imputer_model'  # stores model data and metrics
    )
    return imputer


# TODO: replace with terminal commands somewhere else
bd_config_section = 'DB_INNERWEAR_V1_ORG'
table_name = 'cloth'
datawig_benchmark_test(bd_config_section, table_name, ['brand_name', 'description'], 'brand_name')