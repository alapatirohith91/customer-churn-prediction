import pandas as pd
from sqlalchemy import create_engine

# Load dataset
df = pd.read_csv(r"D:\customer-churn-project\data\processed_churn_data.csv")

# PostgreSQL connection
engine = create_engine(
     "postgresql://postgres:Rohith%402004@localhost:5432/customer_churn_db"
)

# Store data into PostgreSQL
df.to_sql(
    "customers",
    engine,
    if_exists="replace",
    index=False
)

print("Data stored successfully in PostgreSQL!")