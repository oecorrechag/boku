import os
import pandas as pd
import datetime
from sqlalchemy import create_engine
from sklearn.datasets import fetch_california_housing

from mypackage.connect import read_table, upload_data_mysql

ahora = datetime.datetime.now()
print(f'Extrac - La fecha es: {ahora}')

<<<<<<< HEAD
housing_data_raw = pd.read_csv('data/raw/housing_data_raw.csv', 
                               sep = ',', decimal = '.', header = 0, encoding = 'utf-8')
print(f'shape old: {housing_data_raw.shape}')

=======
>>>>>>> 260d4cfc64f303eff6a356285ed8b111fca06fc8
data = fetch_california_housing(as_frame=True)
housing_data_new = data.frame
housing_data_new = housing_data_new.sample(frac=0.005)

BD_KEY = os.getenv("BD_KEY")

# engine = create_engine(f'mysql+pymysql://root:{BD_KEY}@localhost/houses')
# engine = create_engine(f'mysql+pymysql://root:{BD_KEY}@127.0.0.1:3306/houses')
# engine = create_engine(f'mysql+pymysql://root:{BD_KEY}@localhost:3306/houses')
engine = create_engine(f'mysql://root:{BD_KEY}@localhost/houses')

print(f'aca va en eng: {engine}')

query = f"SELECT * FROM raw"
df_old = pd.read_sql_query(query, engine)
print(f"Loaded table: raw")


print(df_old.head())


# df_old = read_table(engine, 'raw')
# print(f'shape actual: {df_old.shape}')

data = fetch_california_housing(as_frame=True)
data_new = data.frame
data_new = data_new.sample(frac=0.0005)
print(f'shape data new: {data_new.shape}')

df = pd.concat([df_old, data_new], ignore_index=True)
print(f'shape new: {df.shape}')

upload_data_mysql(engine, df, 'raw')
