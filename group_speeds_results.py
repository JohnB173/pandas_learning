import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("group_results.xlsx")
df = df.drop(columns=["Package (if known)"])
df = df.set_index("Internet Service Provider")
sorted_df_ascending = df.sort_values(by="Fastest Upload", ascending=False)
sorted_df_decending = df.sort_values(by="Fastest Upload", ascending=True)
# print(sorted_df_decending)
# print(df.info())
# print(df.describe())


# Q1_dl = df["Fastest Download"].quantile(0.25)
# Q3_dl = df["Fastest Download"].quantile(0.75)
# IQR_dl = Q3_dl - Q1_dl
# # print(IQR_dl)
# # 44.77 ------
# Q1_upl = df["Fastest Upload"].quantile(0.25)
# Q3_upl = df["Fastest Upload"].quantile(0.75)
# IQR_upl = Q3_upl - Q1_upl
# # print(IQR_upl)
# # 11.98 ------
# outliers_dl = df[(df<Q1_dl-1.5*IQR_dl) | (df>Q3_dl+1.5*IQR_dl)]
# print(outliers_dl)
# outliers_upl = df[(df<Q1_upl-1.5*IQR_upl) | (df>Q3_upl+1.5*IQR_upl)]
# print(outliers_upl)

# def find_outliers_IQR(df):
#     Q1 = df.quantile(0.25)
#     Q3 = df.quantile(0.75)
#     IQR = Q3 - Q1
#     outliers = df[(df<Q1-1.5*IQR) | (df>Q3+1.5*IQR)]
#     return outliers
# print(find_outliers_IQR(df))
# # now tv 0.41 / utility warehouse 63.59 / virgin media 96.47 all slowest downloads
# outliers_df = find_outliers_IQR(df)
# outliers_df.to_excel("Grp_Spd_Outlier.xlsx", index=False)

# sorted_df_ascending.to_excel("Grp_Spd_Results.xlsx", index=False)

# mean = df.mean()
# print(mean)

mean_upl = df["Mean Upload"].mean()
# # 11.56 mean upload
# print(mean_upl)
mean_dl = df["Mean Download"].mean()
# print(mean_dl)
# # 45.25 mean download
median_upl = df["Median Upload"].median()
# print(median_upl)
# # 10.82 median upload
median_dl = df["Median Download"].median()
# print(median_dl)
# # 36.56 median download

# slowest_dl_speed = df["Slowest Download"].min()
# print(slowest_dl_speed)
# fastest_dl_speed = df["Fastest Download"].max()
# print(fastest_dl_speed)
# slowest_upl_speed = df["Slowest Upload"].min()
# print(slowest_upl_speed)
# fastest_upl_speed = df["Fastest Upload"].max()
# print(fastest_upl_speed)

# def above_mean_dl():
#     return df[df["Mean Download"] > mean_dl]
# print(above_mean_dl())

national_avg_dl = 69.4
df["national_avg_dl"] = national_avg_dl

national_avg_upl = 18.4
df["national_avg_upl"] = national_avg_upl
# data taken from ofcom, national median 
# plt.figure(figsize=(10, 6))

# plt.subplot(2, 2, 1)
# plt.bar(df.index, df['Median Download'], color='green', label='Median Download Speed')
# # set index as ISP
# plt.axhline(y=national_avg_dl, color='red', linestyle='--', label='National Download Median')
# # ofcom red line across
# plt.title('Median DL Speed Comparison')
# plt.xticks(rotation=45)
# # spacing of index appearance 
# plt.ylabel("Mb/s")
# plt.legend()

# plt.subplot(2, 2, 2)
# plt.bar(df.index, df['Median Upload'], color='blue', label='Median Upload Speed')
# plt.axhline(y=national_avg_upl, color='red', linestyle='--', label='National Upload Median')
# plt.title('Median Upload Speed Comparison')
# plt.xticks(rotation=45)
# plt.ylabel("Mb/s")
# plt.legend()

# plt.tight_layout()
# plt.legend()
# plt.show()