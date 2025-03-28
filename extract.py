import pandas as pd
import datetime
from sklearn.datasets import fetch_california_housing

ahora = datetime.datetime.now()
print(f'Extrac - La fecha es: {ahora}')

housing_data_raw = pd.read_csv('data/raw/housing_data_raw.csv', 
                               sep = ',', decimal = '.', header = 0, encoding = 'utf-8')
print(f'shape old: {housing_data_raw.shape}')

data = fetch_california_housing(as_frame=True)
housing_data_new = data.frame
housing_data_new = housing_data_new.sample(frac=0.0005)

df = pd.concat([housing_data_raw, housing_data_new], ignore_index=True)
df.to_csv('data/raw/housing_data_raw.csv', encoding = 'utf-8-sig', index = False)
print(f'shape actual: {df.shape}')
