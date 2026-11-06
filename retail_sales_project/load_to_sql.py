import pandas as pd
import sqlite3

#read cleaned csv
df = pd.read_csv("cleaned_sales.csv")

#connect to sqlite database
connection = sqlite3.connect("retail_sales.db")

# load data into sql table
df.to_sql(
    "sales",
    connection,
    if_exists="replace",
    index = False
    )

#verify records

result = pd.read_sql_query(
    "SELECT * FROM sales", connection
)

print("==== SQL DATABASE LOADED ====")
print("Total records:", len(result))

connection.close()

print("\nDatabase created successfully!")