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

df = df.dropna(how="any")
df = df.set_index("Transaction ID")
print(df)