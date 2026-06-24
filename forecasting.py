from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pandas as pd

df = pd.read_csv("amazon_sales_2025_INR (1).csv")

df['Date'] = pd.to_datetime(df['Date'])

monthly_sales = (
    df.groupby(df['Date'].dt.month)['Total_Sales_INR']
      .sum()
      .reset_index()
)

monthly_sales.columns = ['Month', 'Sales']

print(monthly_sales)

monthly_sales['Previous_Month_Sales'] = monthly_sales['Sales'].shift(1)

monthly_sales = monthly_sales.dropna()

print(monthly_sales)


X = monthly_sales[['Previous_Month_Sales']]
y = monthly_sales['Sales']

model = LinearRegression()

model.fit(X, y)


X = monthly_sales[['Previous_Month_Sales']]
y = monthly_sales['Sales']

model = LinearRegression()

model.fit(X, y)

monthly_sales['Predicted_Sales'] = model.predict(X)

print(monthly_sales)


plt.figure(figsize=(10, 5))

plt.plot(
    monthly_sales['Month'],
    monthly_sales['Sales'],
    marker='o',
    label='Actual Sales'
)

plt.plot(
    monthly_sales['Month'],
    monthly_sales['Predicted_Sales'],
    marker='s',
    label='Predicted Sales'
)

plt.title('Actual vs Predicted Sales')

plt.xlabel('Month')
plt.ylabel('Revenue')

plt.legend()

plt.grid(True)

plt.show()


mae = mean_absolute_error(
    monthly_sales['Sales'],
    monthly_sales['Predicted_Sales']
)

rmse = mean_squared_error(
    monthly_sales['Sales'],
    monthly_sales['Predicted_Sales']
) ** 0.5

print("MAE:", mae)
print("RMSE:", rmse)


mae = mean_absolute_error(
    monthly_sales['Sales'],
    monthly_sales['Predicted_Sales']
)

rmse = mean_squared_error(
    monthly_sales['Sales'],
    monthly_sales['Predicted_Sales']
) ** 0.5

print("MAE:", mae)
print("RMSE:", rmse)
