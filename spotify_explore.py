import pandas as pd

df = pd.read_csv("spotify_songs.csv")
# df.info()
# print(df.shape)
# print(df.columns)
# print(df.head())
# print(df["playlist_genre"].value_counts())
# print(df["playlist_genre"].mode())
# print(df["duration_ms"].median())
# print(df["duration_ms"].mean())

# max_ms = df["duration_ms"].max()
# min_ms = df["duration_ms"].min()
# print (max_ms-min_ms)

# print(df["duration_ms"].sum())

# print(df.sort_values(by=["duration_ms"], ascending=False))

# print(df.sort_values(by=["track_name"]))

# print(df.groupby("playlist_genre")["duration_ms"].min())

# print(df.query("track_artist=='Ricky Martin'"))

mean_val = df["duration_ms"].mean()

print(df.query("duration_ms >@ mean_val"))