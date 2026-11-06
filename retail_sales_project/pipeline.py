import pandas as pd

#step -1 read raw sales data

df= pd.read_csv("raw_sales.csv")

print("RAW SALES DATA :", len(df))




#step -3 fill missing values

df["city"] = df["city"].fillna("Unknown")

#step -4 remove duplicate values

df = df.drop_duplicates(subset=["order_id"], keep ="first")

#step - 5. remove invalid quantities and prices

df = df[
    (df["quantity"]> 0)&
    (df["unit_price"]>0)
].copy()

#6. convert order_date to datetime

df["order_date"] = pd.to_datetime(
    df["order_date"], errors ="coerce"
)

#remove records with invalid dates

df = df.dropna(subset=["order_date"])

#7. calculate total_amount

df["total_amount"] = df["quantity"]*df["unit_price"]

#8. save cleaned data
df.to_csv("cleaned_sales.csv", index = False)

#9. dislay results

print("\n==== CLEANING SUMMARY ====")
print("FInal records:", len(df))
print("Missing Cities:", df["city"].isnull().sum())
print("Duplicate order IDs:", df.duplicated(subset=["order_id"]).sum())
print("Incalid Quantities:", (df["quantity"] < 0).sum())

print("\n==== CLEANED SALES DATA ====")
print(df)

print("\nCleaned data saved successfully!")