import pandas as pd
# pd.set_option("display.max_rows", 147)
df = pd.read_csv("results.csv")
# # print(df)
# df.info()
# print(df.describe())
# # print(df["home_score"].value_counts())
# # print(df["home_score"].value_counts(normalize=True)*100)
# mask = df["home_score"] < 7
# masked_df = df[mask]
# print(masked_df["home_score"].mean())
# print(df.sort_values(["tournament"]))

# Activity 1

# print(df["tournament"].value_counts())
 # # 147 tournaments played from lowest 1 to highest 17773
# print(df["home_team"].value_counts())
# Brazil 600 home
# print(df["away_team"].value_counts())
# Uruguay 565
# print(df["home_team"].max())
# print(df["away_team"].max())
# Aland Islands
# print(df["home_team"].min())
# print(df["away_team"].min())
# Abkhazia
# count = df[(df['country'] == "England") & (df['home_team'] == "England")]
# print(count)
# 474 rows, 45202 england england
mean_goal = df[(df["country"] == "England")].mean()
print(df.query("England >@ mean_goal"))

# goalscorers

# df = pd.read_csv("goalscorers.csv")
# # print(df.describe())
# # print(df["penalty"].value_counts(normalize=True)*100)
# # print(df["scorer"].value_counts())
# mask = df["minute"] < 90
# masked_df = df[mask]
# print(masked_df["minute"].mean())

# shootouts

# df = pd.read_csv("shootouts.csv")
# # print(df.describe())
# print(df["winner"].value_counts())

# spotify

# df = pd.read_csv("spotify_songs.csv")
# print(df.describe())
# print(df["track_name"].value_counts())