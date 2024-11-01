import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

Monday_df = pd.read_excel("monday_voucher_data.xlsx")
Tuesday_df = pd.read_excel("tuesday_voucher_data.xlsx")
Wednesday_df = pd.read_excel("wednesday_voucher_data.xlsx")
Thursday_df = pd.read_excel("thursday_voucher_data.xlsx")
Friday_df = pd.read_excel("friday_voucher_data.xlsx")
Saturday_df = pd.read_excel("saturday_voucher_data.xlsx")
Sunday_df = pd.read_excel("sunday_voucher_data.xlsx")

df = pd.concat([Monday_df , Tuesday_df , Wednesday_df , Thursday_df , Friday_df , Saturday_df , Sunday_df], axis=0)

# print(df)

df["New Transaction ID"] = range(1, len(df["Transaction ID"])+1)
# print(df)
df = df.set_index("New Transaction ID")
df = df.drop(columns = ["Transaction ID", "Staff", "Transaction Type"])

df = df.dropna(how = "any")
df["Payment Method"] = df["Payment Method"].str.upper()
df["Basket"] = df["Basket"].str.upper()
# print(df["Basket"].value_counts())



def split_basket(string):
    items = string.split(",")
    stripped_items = [item.strip() for item in items]
    return stripped_items

df["Basket"] = df["Basket"].apply(split_basket)

# print(df.head(5))
# print(df.describe())
# print(df.info())


exploded_data_df = df.explode("Basket", ignore_index=False) 
# print(exploded_data_df["Basket"])



# ...................................................................................................................
# 1st Question:             How many sales were made on each payment type? Ticked
# ...................................................................................................................
# print(df["Payment Method"].value_counts())

# Payment Method
# Debit             165
# Cash              102
# Credit            67
# Voucher           33
# Mobile Wallet     31


# data = { "Payment Method": ["Debit", "Cash", "Credit", "Voucher", "Mobile Wallet"],
#         "Count": [165, 102, 67, 33, 31]}
# df = pd.DataFrame(data)
# plt.figure(figsize=(8, 4))
# plt.bar(df["Payment Method"], df["Count"], color= "blue")
# plt.xlabel("Payment Method")
# plt.ylabel("Sales amount")
# plt.title("Number of Sales by Payment Method")
# plt.grid(False)
# plt.show()



# ..................................................................................................................
# 2nd Question:          How many unique items were paid for by each payment type?
# ..................................................................................................................

# print(df["Total Items"].sum())  # 1514 
# print(df.groupby("Payment Method")["Total Items"].sum()) 

# Payment Method
# Cash             395.0
# Credit           246.0
# Debit            650.0
# Mobile Wallet     97.0
# Voucher          126.0

# Counting each item by each payment method
# Standardize 'Payment Method' values to title case for consistency
df['Payment Method'] = df['Payment Method'].str.title()

# Get all unique items across baskets
unique_items = set(item for basket in df['Basket'] for item in basket)

# Initialize an empty dictionary to store counts
item_payment_counts = {}

# Loop over each unique item and payment method
for item in unique_items:
    item_payment_counts[item] = {}
    for method in df['Payment Method'].unique():
        # Count orders that include the item and use the payment method
        count = df[(df['Payment Method'] == method) & 
                     (df['Basket'].apply(lambda items: item in items))].shape[0]
        item_payment_counts[item][method] = count

# Display the results in a DataFrame for readability
item_payment_counts_df = pd.DataFrame(item_payment_counts).T
# print(item_payment_counts_df)

# Cash  Debit  Mobile Wallet  Credit  Voucher
# Croissant         8     11              3       3        1
# Muffin            4     14              1       2        2
# Tea              42     74              8      30       12
# Stroopwafel       6     12              2       1        1
# Toast             6     10              0       3        1
# Hot Chocolate    45     69             17      33       15
# Latte            48     66             11      30       18
# Buttered Roll     7     12              2       4        2
# Panini            3      9              2       2        1
# Cappuccino       47     70              8      35       18
# Mocha            44     80              9      21       20
# Gift Voucher      0      7              1       3        0
# Americano        46     66             13      24       10


# for method in item_payment_counts_df.columns:
#     plt.scatter(item_payment_counts_df.index, item_payment_counts_df[method], label=method)
# plt.xlabel("Unique Items")
# plt.ylabel("Amount")
# plt.xticks(rotation=90)
# plt.title("Number of Unique Items by Payment Method")
# plt.grid(True)
# plt.legend(title="Payment Method")
# plt.show()









# .................................................................................................................
# 3rd Question:        What percentage of income made came from vouchers?
# .................................................................................................................

# payment_total = df.groupby("Payment Method")["Cost"].sum()
# print(payment_total)
# payment_percentage = (payment_total / payment_total.sum()) * 100

# print(payment_percentage)


# Payment Method
# Cash              684.2  / 23.85%
# Credit            519.5  / 18.10%
# Debit            1237.8  / 43.14%
# Mobile Wallet     198.4  / 6.91%
# Voucher           228.7  / 7.97%


# Group by 'Payment Method' and calculate total income per method
# income_by_payment = df.groupby('Payment Method')['Cost'].sum()

# average_spend = df.groupby("Payment Method")["Cost"].mean()
# # print(average_spend)
# colors = ["blue", "green", "red", "purple", "orange"]
# plt.bar(average_spend.index, average_spend, color=colors[:len(average_spend)])
# for index, value in enumerate(average_spend):
#     plt.text(index, value, f"{value:.2f}", ha="center", va="bottom")
# plt.xlabel("Payment Method")
# plt.ylabel("Average Spent Per Transaction (£)")
# plt.title("Average Spend by Payment Method")
# plt.show()

# Plot the pie chart
# plt.figure(figsize=(8, 8))
# plt.pie(income_by_payment, labels=income_by_payment.index, autopct='%1.1f%%', startangle=140)
# plt.title("Percentage of Income by Payment Method")
# plt.show()

# cost_per_voucher = 0.91
# vouchers_per_week = 33
# weekly_income = 228.7
# software_cost = 1051


# weekly_voucher_cost = vouchers_per_week * cost_per_voucher
# weekly_profit = weekly_income - weekly_voucher_cost
# print(weekly_profit) 198.67

# weeks = np.arange(1, 27)
# # numerical range half a year
# profit = np.cumsum([weekly_profit] * len(weeks)) - software_cost
# # np.cumsum returns the cumalative sum
# plt.figure(figsize=(10, 6))
# # width then height
# plt.plot(weeks, profit, label="Cumulative Profit")
# plt.axhline(0, color='gray', linestyle='--', label="Break-even Point")

# plt.xlabel("Weeks")
# plt.ylabel("Cumulative Profit from Investment (£)")
# plt.title("Voucher Cumulative Profit Over Time")
# plt.legend()
# plt.grid(True)
# plt.show()
# plt.savefig("Voucher_Profit.jpeg")

# 33 vouchers per week make the income 228.7 £. 
# We bought them for 33 * 0.91 to 33 * 2 (30 to 66) £. +25/3 >>>> 38 to 74 £ 
# So they worth it. 
# 1051 for the software x * (228.7 - 56) = 1051 >>>>>> after 6 weeks, using VOUCHERS can benefit the store.


