import pandas as pd
import numpy as np
import datetime
from sklearn.datasets import fetch_california_housing

ahora = datetime.datetime.now()

# Load raw data
housing_data_raw = pd.read_csv('data/raw/housing_data_raw.csv', 
                               sep = ',', decimal = '.', header = 0, encoding = 'utf-8')

def comprobar(df):
    if df.shape[0]>500:

        data = fetch_california_housing(as_frame=True)
        housing_data = data.frame
        housing_data = housing_data.sample(frac=0.0005)
        housing_data.to_csv('data/raw/housing_data_raw.csv', encoding = 'utf-8-sig', index = False)

        housing_data.rename(columns={'MedHouseVal': 'target'}, inplace=True)
        housing_data['prediction'] = housing_data['target'].values + np.random.normal(0, 5, housing_data.shape[0])
        housing_data.to_csv('data/transform/housing_data_clean.csv', encoding = 'utf-8-sig', index = False)
        print(f'Reset - La fecha es: {ahora}')

    else:
        print(f'dim now housing_data_raw: {housing_data_raw.shape}')
        print(f'La dim actual: {df.shape}')
