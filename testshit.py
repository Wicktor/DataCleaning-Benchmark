import pandas as pd
import util.transfer as tf

# df = pd.DataFrame({
#     'A a':'abcdefg',
#     'B b': 1.0,
#     'C c': 1,
#     'D d': ['a', 'b'],
#     'E e': ['a1', 'b'],
#     'F f': [1, 2],
#     'G g': ['a', 1],
# })
# df = pd.read_csv('H:\#Masterarbeit\Datasets\Inner_Wear\\us_topshop_com.csv')
# print(df.columns)
# df.columns = df.columns.str.replace(' ', '_')
# print(df.columns)
# print(df.iloc[0]['A a'])

class TestShitClass():
    def __init__(self, id, name):
        self.id = id
        self.name = name

NewClass = type('new_class', (TestShitClass,), {'lala': 'no_lala'})
new_class_obj = NewClass(1, 'parent_attribute')
print(type(new_class_obj))
print(new_class_obj.lala)
print(new_class_obj.id)
print(new_class_obj.name)

# testClass = TestShitClass(1, 'bla')
# for k, v in vars(testClass).items():
#     print(k, v)


#tf.transfer_csv_to_db('H:\#Masterarbeit\Datasets\Inner_Wear\#inner_wear.csv', 'cloth', 'none')
