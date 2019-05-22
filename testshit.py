import pandas as pd

df = pd.DataFrame({
    'A':'abcdefg',
    'B': 1.0,
    'C': 1,
    'D': ['a', 'b'],
    'E': ['a1', 'b'],
    'F': [1, 2],
    'G': ['a', 1],
})
df = pd.read_csv('H:\#Masterarbeit\Datasets\Inner_Wear\\us_topshop_com.csv')
print(df.dtypes)