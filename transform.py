import pandas as pd
import numpy as np
import datetime

ahora = datetime.datetime.now()
print(f'Transform - La fecha es: {ahora}')

# Load raw data
housing_data_raw = pd.read_csv('data/raw/housing_data_raw.csv', 
                               sep = ',', decimal = '.', header = 0, encoding = 'utf-8')
print(f'dim now housing_data_raw: {housing_data_raw.shape}')

# Perform transformation
housing_data_raw.rename(columns={'MedHouseVal': 'target'}, inplace=True)
housing_data_raw['prediction'] = housing_data_raw['target'].values + np.random.normal(0, 5, housing_data_raw.shape[0])

housing_data_clean = pd.read_csv('data/transform/housing_data_clean.csv', 
                                 sep = ',', decimal = '.', header = 0, encoding = 'utf-8')
print(f'dim now housing_data_clean: {housing_data_clean.shape}')

df = pd.concat([housing_data_raw, housing_data_clean], ignore_index=True)
print(f'dim now df: {df.shape}')

df.to_csv('data/transform/housing_data_clean.csv', encoding = 'utf-8-sig', index = False)

print(f'shape actual: {df.shape}')
