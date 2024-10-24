import pandas as pd
pd.set_option("display.max_rows", 30)
df = pd.read_excel("first_hour_sales.xlsx")
# print(df.describe())
# print(df.info())
df = df.set_index("Transaction ID")
# setting the index to column 
df = df.drop(columns=["Till ID"])
# drop/removing the column named till id
df = df.dropna(how="any")
# drop/removing NaN values from the data
# print(df[df.duplicated()])
# shows duplicated rows
df = df.drop_duplicates()
# drop/removing duplicated rows
df.at[15.0, "Cost"] = 6.00
# changing outlier at row 15 in column cost from 600 to 6

def float_to_time(time_record):
    time_record = str(time_record)
    #convert to string
    hours,minutes = time_record.split('.')
    # split the input at decimal
    timestamp = f"{int(hours):02}:{int(minutes):02}"
    # HH/MM
    return timestamp

df["Time"] = df["Time"].apply(float_to_time)
# apply the function defined to change the format
df["Time"] = pd.to_datetime(df["Time"])
# changes the data type to datetime64

def split_basket(basket_item):
    items = basket_item.split(",")
    stripped_items = [item.strip() for item in items]
    return (stripped_items)

df["Basket"] = df["Basket"].apply(split_basket)
# print(df["Basket"])
exploded_data = df.explode("Basket", ignore_index=False)
# print(exploded_data["Basket"])
# print(df.info())

# # Activity 1


# print(exploded_data["Cost"].mean())
# # 8.52 avg cost
# avg_cost = exploded_data.groupby("Basket")["Cost"].mean()
# print(avg_cost)
# highest_spend = exploded_data.groupby("Transaction ID")["Cost"].max()
# print(highest_spend)
# max_spend = df["Cost"].max()
# print(max_spend)
# # highest spend transaction 24 at 12
# minimum_spend = exploded_data.groupby("Transaction ID")["Cost"].min()
# print(minimum_spend)
# min spend transaction 21 at 1.9

# print(exploded_data["Cost"].value_counts())
# # 7.5, 8 times most common spend amount
# print(exploded_data["Payment Method"].value_counts())
# # 49 times, debit most common type
