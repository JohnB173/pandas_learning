import pandas as pd
import matplotlib.pyplot as plt
monday_df = pd.read_excel('monday_voucher_data.xlsx')
tuesday_df = pd.read_excel('tuesday_voucher_data.xlsx')
wednesday_df = pd.read_excel('wednesday_voucher_data.xlsx')
thursday_df = pd.read_excel('thursday_voucher_data.xlsx')
friday_df = pd.read_excel('friday_voucher_data.xlsx')
saturday_df = pd.read_excel('saturday_voucher_data.xlsx')
sunday_df = pd.read_excel('sunday_voucher_data.xlsx')
df = pd.concat([monday_df , tuesday_df , wednesday_df , thursday_df , friday_df , saturday_df , sunday_df], axis=0)
# print(df)
# print(df.info())
# print(df.describe())


# print(df)

df["New Transaction ID"] = range(1, len(df["Transaction ID"])+1)
# print(df)

df = df.set_index("New Transaction ID")
df = df.dropna(how = "any")
# print(df)
df = df.drop(columns=["Transaction ID", "Staff", "Transaction Type"])

def split_basket(string):
    items = string.split(",")
    stripped_items = [item.strip() for item in items]
    return stripped_items

df["Basket"] = df["Basket"].apply(split_basket)

# print(df.head(5))
# print(df.describe())
# print(df.info())

exploded_data_df = df.explode("Basket", ignore_index=False) 
print(exploded_data_df["Basket"])