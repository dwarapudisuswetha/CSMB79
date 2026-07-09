import pandas as pd

df = pd.read_csv("Messy_Employee_dataset.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

print("\nDuplicate Records:")
print(df.duplicated().sum())

# Fill missing values

# Fill missing Age with median
df["Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing Salary with mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Check missing values again
print("\nMissing Values After Filling:")
print(df.isnull().sum())