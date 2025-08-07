import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the file
df = pd.read_csv("C:/Users/gulna/Downloads/archive/supply_chain_deliveries.csv")

# View first 5 rows
print(df.head())

# Data structure info
print("--- Data Info ---")
print(df.info())

# Statistical summary
print("--- Statistical Summary ---")
print(df.describe())

# Number of missing values
print("--- Missing Values ---")
print(df.isnull().sum())

# Number of duplicate rows
print("--- Duplicate Rows ---")
print(df.duplicated().sum())

# Column names
print("--- Column Names ---")
print(df.columns)

# Top 10 most frequent locations
print("--- Top 10 Locations by Order Count ---")
top_locations = df["Location"].value_counts().head(10)
print(top_locations)

# Top customers by order count
print("--- Orders by Customer ---")
print(df["Customer"].value_counts())

# Bar chart for top 10 locations
plt.figure(figsize=(10, 6))
sns.barplot(x=top_locations.index, y=top_locations.values)
plt.xticks(rotation=45)
plt.title("Top 10 Most Frequent Order Locations")
plt.xlabel("Location")
plt.ylabel("Order Count")
plt.tight_layout()
plt.show()

# Total orders by customer
orders_by_customer = df.groupby("Customer")["OrderCount"].sum().sort_values(ascending=False)

# Total revenue by customer
revenue_by_customer = df.groupby("Customer")["TotalRevenue"].sum().sort_values(ascending=False)

# Top 5 customers by order count
print("--- Top 5 Customers by Order Count ---")
print(orders_by_customer.head())

# Top 5 customers by revenue
print("-- Top 5 Customers by Revenue ---")
print(revenue_by_customer.head())
