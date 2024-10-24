import pandas as pd

df = pd.read_excel("group_results.xlsx")
df = df.drop(columns=["Package (if known)"])
df = df.set_index("Internet Service Provider")
sorted_df = df.sort_values(by="Fastest Upload", ascending=False)
# print(sorted_df)

mean_upl = df["Mean Upload"].mean()
# 11.56
print(mean_upl)