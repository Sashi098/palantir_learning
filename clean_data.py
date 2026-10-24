import pandas as pd

# read the csv file
df = pd.read_csv("customers.csv")

#display the original data
print("Original Data:")
print(df)

# find missing values in each column
print("\n MIssing values:")
print(df.isnull().sum())


# replace missing customer names
df["customer_name"] = df["customer_name"].fillna("Unknown")

#display cleaned data
print("\n Cleaned Data:")
print(df)

#check missing values again
print("\nMissing values after cleaning:")
print(df.isnull().sum())

df["city"] = df['city'].fillna("Unknown")

print("\nFinal cleaned data")
print(df)

print("\nMssing values:")
print(df.isnull().sum())

#save cleaned data to new csv file
df.to_csv("cleaned_customers.csv", index=False)

print ("\nCleaned data saved successfully!")