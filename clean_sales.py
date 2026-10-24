import pandas as pd

df = pd.read_csv("sales.csv")

print("\nOriginal Data:")
print(df)

print("\nMissing vales:")
print(df.isnull().sum())

df['product'] = df["product"].fillna("Unknown")
df["city"] = df["city"].fillna("Unknown")

#remove rows where price is missing
df = df.dropna(subset=["price"])

# remove duplicate rows
df = df.drop_duplicates(
    subset=["product", "quantity", "price", "city"]
)

#save cleaned data
df.to_csv("cleaned_sales.csv", index=False)

print("|nCLeaned Data:")
print(df)

print("\nMissing values after cleaning :")
print(df.isnull().sum())