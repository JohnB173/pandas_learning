import pandas as pd

df = pd.read_excel("results2024-10-24-159.xlsx")

# sorted_df = df.sort_values(by="Upload (Mb/s)", ascending=False)
# print(sorted_df)

mean_dl = df["Download (Mb/s)"].mean()
# print(mean_dl)
# 36.76 ----- mean dl speed ------

mean_upl = df["Upload (Mb/s)"].mean()
# print(mean_upl)
# 22.58 ----- mean upload speed -------

median_dl = df["Download (Mb/s)"].median()
# print(median_dl)
# 36.56 ----- median dl speed -------

median_upl = df["Upload (Mb/s)"].median()
# print(median_upl)
# 24.54 --------- median upload speed -------


# def above_mean_dl():
#     return df[df["Download (Mb/s)"] > mean_dl]
# print(above_mean_dl())

# slowest_speed = df["Download (Mb/s)"].min()
# print(slowest_speed)
# # 28.98 -------

# highest_speed = df["Download (Mb/s)"].max()
# print(highest_speed)
# 44.70 --------

# fast_upload = df["Upload (Mb/s)"].max()
# print(fast_upload)
# # 26.86 --------

# slow_upload = df["Upload (Mb/s)"].min()
# print(slow_upload)
# # 12.10 --------