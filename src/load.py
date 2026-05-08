import pandas as pd
from sqlalchemy import create_engine

# Load transformed CSV
df = pd.read_csv(r"c:\Users\user\ipl_2025\data\processed\cleaned_ipl_2025.csv")

# SQL Server connection
#replace \ with r or \\
server = r"LAPTOP-VMI43L37\SQLEXPRESS"
database = "IPL_2025"

connection_string = (
    f"mssql+pyodbc://{server}/{database}"
    "?driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

engine = create_engine(connection_string)

# Load data into SQL table
df.to_sql(
    name="ipl_matches",
    con=engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully into SQL Server")