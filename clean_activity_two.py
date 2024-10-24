import pandas as pd
# pd.set_option("display.max_rows", 100)
df = pd.read_excel("cleaning_activity.xlsx")

df = df.set_index("Transaction ID")
df = df.drop(columns=["Till ID"]+["Unnamed: 0"])
df = df.dropna(how="any")
# print(df[df.duplicated()])
df = df.drop_duplicates()
df.at[56.0, "Cost"] = 6.00

# print(df.describe())
# print(df.info())
# print(df["Cost"].mean())
# 6.6
avg_cost = df.groupby("Basket")["Cost"].mean()
print(avg_cost)