import pandas as pd
from ydata_profiling import ProfileReport

# df = pd.read_csv("results.csv")

# profile = ProfileReport(df, title="Football Results")

# profile.to_file("results_report.html")


# goalscorers

# df = pd.read_csv("goalscorers.csv")

# profile = ProfileReport(df, title="Goalscorers_Results")

# profile.to_file("results_report.html")


# shootouts

# df = pd.read_csv("shootouts.csv")
# profile = ProfileReport(df, title="shootout_results")
# profile.to_file("shootout_results.html")

# spotify

df = pd.read_csv("spotify_songs.csv")
profile = ProfileReport(df, title="Spoifty_songs_results")
profile.to_file("spotify_song_results.html")