import pandas as pd

print("=== SALES ETL PIPELINE STARTED ===")

#extract

df = pd.read_csv("sales.csv")
print("Step-1: Raw data loaded:", len(df), "rows")

#transform: convert numeric column

df["quantity"] = pd.to_numeric(df["quantity"], errors= "coerce")
df["price"] = pd.to_numeric(df["price"], errors= "coerce")

#remove rows missing required numeric values

df= df.dropna(subset=["quantity","price"]).copy()

#replace missing text values

df["product"] = df["product"].fillna("Unknown")
df["city"] = df["city"].fillna("Unknown")

#remove duplicate order Ids

df = df.drop_duplicates(subset=["order_id"]).copy()

#create calculated column
df["total_amount"] = df["quantity"]* df["price"]

print("Step-2: Data transformation completed")

#validated: check data quality
valid = (
    df["order_id"].notna().all()
    and df["quantity"].ge(0).all()
    and df["price"].ge(0).all()
    and df["total_amount"].notna().all()
    and df["order_id"].is_unique
)

if not valid:
    raise ValueError("Validation failed! Check the sales data.")

print("Step-3: Validation passed")
print("Rows ready to save:", len(df))

# load: save the final output
df.to_csv("Final_sales.csv", index= False)

print("Step-4 : Data daved to final_sales.csv")
print("=== SALES ETL PIPELINE COMPLETED ===")