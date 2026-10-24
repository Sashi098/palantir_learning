import pandas as pd

df= pd.read_csv("cleaned_sales.csv")

print("Original Data:")
print (df)

# convert quantity and price to numeric values
df["quantity"] = pd.to_numeric(df["quantity"],errors="coerce")
df["price"] = pd.to_numeric(df["price"], errors="coerce")

#create a calculated column
df["total_amount"] = df["quantity"]* df["price"]

#validate the transformed data
print("\nData validation:")

print("Missing values:")
print(df.isnull().sum())

print("\nNegative quantities:", (df["quantity"]< 0).sum())
print("Negative prices:", (df["price"]< 0).sum())

print("\nDUplicate order IDs:", df["order_id"].duplicated().sum())

#check calculated totals
expected_total = df["quantity"]* df["price"]
print(
    "All totals correct:",
    df["total_amount"].equals(expected_total)
)

product_sales = df.groupby("product")["total_amount"].sum()
print(product_sales)

print("\nTransformed Data:")
print(df[["order_id","product","quantity","price","total_amount"]])

#save transformed data
df.to_csv("transformed_sales.csv", index=False)

print("\nTransformed data saved successfully!")