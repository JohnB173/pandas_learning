import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("group_results.xlsx")
df = df.drop(columns=["Package (if known)"])
df = df.set_index("Internet Service Provider")
sorted_df_ascending = df.sort_values(by="Fastest Upload", ascending=False)
sorted_df_decending = df.sort_values(by="Fastest Upload", ascending=True)
# print(sorted_df_decending)


# mean_upl = df["Mean Upload"].mean()
# # 11.56 mean upload
# print(mean_upl)
mean_dl = df["Mean Download"].mean()
# print(mean_dl)
# # 45.25 mean download
# median_upl = df["Median Upload"].median()
# print(median_upl)
# # 10.82 median upload
# median_dl = df["Median Download"].median()
# print(median_dl)
# # 36.56 median download

# def above_mean_dl():
#     return df[df["Mean Download"] > mean_dl]
# print(above_mean_dl())

national_avg_dl = 69.4
df["national_avg_dl"] = national_avg_dl

national_avg_upl = 18.4
df["national_avg_upl"] = national_avg_upl

plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
plt.bar(df.index, df['Median Download'], color='green', label='Median Download Speed')
plt.axhline(y=national_avg_dl, color='red', linestyle='--', label='National Download Median')
plt.title('Median DL Speed Comparison')
plt.xticks(rotation=45)
plt.ylabel("Mb/s")
plt.legend()

plt.subplot(2, 2, 2)
plt.bar(df.index, df['Median Upload'], color='blue', label='Median Upload Speed')
plt.axhline(y=national_avg_upl, color='red', linestyle='--', label='National Upload Median')
plt.title('Median Upload Speed Comparison')
plt.xticks(rotation=45)
plt.ylabel("Mb/s")
plt.legend()

plt.tight_layout()
plt.legend()
plt.show()