import persistance.db_operator as db_op

def clean_column_string_values(db_config_section, mapped_class, column_name:str, search_substring, replacement_string):
    cloths = db_op.db_get_all_entrys_of(db_config_section, mapped_class)
    cloths_to_save = []
    for cloth in cloths:
        try:
         attr_value = getattr(cloth, column_name)
         if search_substring.lower() in attr_value.lower():
             setattr(cloth, column_name, replacement_string)
             cloths_to_save.append(cloth)
        except:
            print('Attribut/Column '+ column_name + 'for Class/Table ' + '' + 'not found')  # TODO: insert class/table name
            return

    db_op.db_save(cloths_to_save, db_config_section)