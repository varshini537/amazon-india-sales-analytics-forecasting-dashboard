import matplotlib.pyplot as plt
import pandas as pd

# Load dataset
df = pd.read_csv('amazon_sales_2025_INR (1).csv')

# Dataset overview
print("Shape:", df.shape)

print("\nColumns:")
print(df.columns)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Create new columns
df['Month'] = df['Date'].dt.month_name()
df['Month_Number'] = df['Date'].dt.month
df['Quarter'] = df['Date'].dt.quarter

print("\nDate conversion successful!")
df.to_csv("cleaned_amazon_sales.csv", index=False)

print("Cleaned dataset saved!")

total_sales = df['Total_Sales_INR'].sum()
total_orders = df['Order_ID'].nunique()
total_customers = df['Customer_ID'].nunique()
avg_rating = df['Review_Rating'].mean()

print("\n===== KPI SUMMARY =====")
print("Total Revenue:", total_sales)
print("Total Orders:", total_orders)
print("Total Customers:", total_customers)
print("Average Rating:", round(avg_rating, 2))

category_sales = (
    df.groupby('Product_Category')['Total_Sales_INR']
      .sum()
      .sort_values(ascending=False)
)

print(category_sales)

state_sales = (
    df.groupby('State')['Total_Sales_INR']
      .sum()
      .sort_values(ascending=False)
)

print(state_sales.head(10))

print("Starting Payment Analysis...")

payment_sales = (
    df.groupby('Payment_Method')['Total_Sales_INR']
      .sum()
      .sort_values(ascending=False)
)

print(payment_sales)

print(df['Delivery_Status'].value_counts())

rating_dist = df['Review_Rating'].value_counts().sort_index()

print(rating_dist)
category_rating = (
    df.groupby('Product_Category')['Review_Rating']
      .mean()
      .sort_values(ascending=False)
)

print(category_rating)

category_sales.plot(kind='bar')

plt.title('Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Revenue (INR)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
print("Payment Analysis Complete")

state_sales = (
    df.groupby('State')['Total_Sales_INR']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)


plt.figure(figsize=(10, 6))

state_sales.plot(kind='bar')

plt.title('Top 10 States by Revenue')
plt.xlabel('State')
plt.ylabel('Revenue (INR)')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))

payment_sales = (
    df.groupby('Payment_Method')['Total_Sales_INR']
      .sum()
      .sort_values(ascending=False)
)

print(payment_sales)


ax = payment_sales.plot(
    kind='bar',
    figsize=(8, 5)
)

ax.set_title('Revenue by Payment Method')
ax.set_xlabel('Payment Method')
ax.set_ylabel('Revenue (INR)')

plt.tight_layout()
plt.show()

delivery_status = df['Delivery_Status'].value_counts()

print(delivery_status)

plt.figure(figsize=(8, 5))

delivery_status.plot(kind='bar')

plt.title('Delivery Status Distribution')
plt.xlabel('Status')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

rating_dist = df['Review_Rating'].value_counts().sort_index()

print(rating_dist)

plt.figure(figsize=(8, 5))

rating_dist.plot(kind='bar')

plt.title('Customer Rating Distribution')
plt.xlabel('Rating')
plt.ylabel('Count')

plt.tight_layout()
plt.show()

monthly_sales = (
    df.groupby('Month_Number')['Total_Sales_INR']
      .sum()
)

print(monthly_sales)

ax = monthly_sales.plot(
    kind='line',
    marker='o',
    figsize=(10, 5)
)

ax.set_title('Monthly Sales Trend')
ax.set_xlabel('Month')
ax.set_ylabel('Revenue (INR)')

plt.tight_layout()
plt.show()

rating_dist = df['Review_Rating'].value_counts().sort_index()

print(rating_dist)

ax = rating_dist.plot(
    kind='bar',
    figsize=(8, 5)
)

ax.set_title('Customer Rating Distribution')
ax.set_xlabel('Rating')
ax.set_ylabel('Count')

plt.tight_layout()
plt.show()

monthly_sales = (
    df.groupby('Month_Number')['Total_Sales_INR']
      .sum()
)

print(monthly_sales)

ax = monthly_sales.plot(
    kind='line',
    marker='o',
    figsize=(10, 5)
)

ax.set_title('Monthly Sales Trend')
ax.set_xlabel('Month')
ax.set_ylabel('Revenue (INR)')

plt.tight_layout()
plt.show()
top_products = (
    df.groupby('Product_Name')['Total_Sales_INR']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

print(top_products)

ax = top_products.plot(
    kind='bar',
    figsize=(10, 5)
)

ax.set_title('Top 10 Products by Revenue')
ax.set_xlabel('Product')
ax.set_ylabel('Revenue (INR)')

plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
