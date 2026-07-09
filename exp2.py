import pandas as pd

# Read datasets
titanic = pd.read_csv("train.csv")
iris = pd.read_csv(
    "iris.csv",
    names=["SepalLength","SepalWidth","PetalLength","PetalWidth","Species"]
)
# Display first 5 rows
print("Titanic Dataset:")
print(titanic.head())

print("\nIris Dataset:")
print(iris.head())

# Titanic statistics
age = titanic["Age"].fillna(titanic["Age"].mean())
fare = titanic["Fare"]

print("\nTitanic Statistics")
print("Age Mean:", age.mean())
print("Age Median:", age.median())
print("Age Mode:", age.mode()[0])

print("Fare Mean:", fare.mean())
print("Fare Median:", fare.median())
print("Fare Mode:", fare.mode()[0])