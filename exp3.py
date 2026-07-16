import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("Messy_Employee_dataset.csv")

# Display first 5 rows
print(df.head())

# Dataset information
print(df.info())

# Check missing values
print(df.isnull().sum())

# Check duplicate rows
print(df.duplicated().sum())

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# Check missing values again
print(df.isnull().sum())

# Box plot
plt.boxplot(df["Salary"])
plt.title("Salary Box Plot")
plt.ylabel("Salary")
plt.show()

# ---------- IQR CODE STARTS HERE ----------

Q1 = df["Salary"].quantile(0.25)
Q3 = df["Salary"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

outliers = df[(df["Salary"] < lower_limit) | (df["Salary"] > upper_limit)]

print("Q1 =", Q1)
print("Q3 =", Q3)
print("IQR =", IQR)
print("Lower Limit =", lower_limit)
print("Upper Limit =", upper_limit)
print("Number of Outliers =", len(outliers))