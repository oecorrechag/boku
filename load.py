import json
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# Connect to database
engine = create_engine("postgresql://myuser:mypassword@localhost:5432/mydatabase")

# Create metadata object
metadata = MetaData()

# Define table schema
mytable = Table(
    "mytable",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("column1", String),
    Column("column2", String),
)

# Read transformed data from file
with open("transformed_data.json", "r") as f:
    data = json.load(f)

# Load data into database
with engine.connect() as conn:
    for item in data:
        conn.execute(
            mytable.insert().values(column1=item["column1"], column2=item["column2"])
        )
        