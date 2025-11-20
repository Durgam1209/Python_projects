import pandas as pd
import matplotlib.pyplot as plt


df= pd.read_csv('Coffe_sales.csv')

#1. Coffee sales distribution
plt.figure(figsize=(8,5))
df['coffee_name'].value_counts().plot(kind='bar')
plt.title("Number of Orders per Coffee Type")
plt.xlabel("Coffee Type")
plt.ylabel("Order Count")
plt.tight_layout()
plt.show()


#2. Total revenue per coffee
plt.figure(figsize=(8,5))
df.groupby('coffee_name')['money'].sum().plot(kind='bar')
plt.title("Total Revenue per Coffee Type")
plt.xlabel("Coffee Type")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()

#3 Sales Distribution by Time of Day

plt.figure(figsize=(8,5))
df.groupby('Time_of_Day')['money'].sum().plot(kind='bar')
plt.title("Orders by Time of day")
plt.xlabel("Time of Day")
plt.ylabel("Orders")
plt.tight_layout()
plt.show()

#4 Hourly Sales distrbution
plt.figure(figsize=(8,5))
df.groupby('hour_of_day')['money'].sum().plot(kind='bar')
plt.title("Orders by Time of day")
plt.xlabel("Time of Day")
plt.ylabel("Orders")
plt.tight_layout()
plt.show()

# 5. Sales by Weekday (using sorted order)
plt.figure(figsize=(8,5))
weekday_sales = df.groupby(['Weekdaysort','Weekday'])['money'].sum().reset_index()
weekday_sales.sort_values('Weekdaysort').set_index('Weekday')['money'].plot(kind='bar')
plt.title("Sales by Weekday")
plt.xlabel("Weekday")
plt.ylabel("Total Revenue")
plt.tight_layout()
plt.show()
