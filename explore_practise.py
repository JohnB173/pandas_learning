import pandas as pd
# pd.set_option("display.max_rows", 147)
# # stops truncating results by changing value
df = pd.read_csv("results.csv")
# print(df)
# df.info()
# # shows columns and data types
# print(df.describe())
# # shows mean standard deviation range 
# print(df["home_score"].value_counts())
# # counts how many times a goal was scored
# print(df["home_score"].value_counts(normalize=True)*100)
# # normalize=true*100 turns the count into percentages
# mask = df["home_score"] < 7
# # boolean mask where homescore is less than 7
# masked_df = df[mask]
# # apply mask to dataframe to filter out scores above 7
# print(masked_df["home_score"].mean())
# # print the masked dataframe homescore average
# print(df.sort_values(["tournament"]))

# Activity 1

# print(df["tournament"].value_counts())
#  # 147 tournaments played from lowest 1 to highest 17773
# unique_tournament = df["tournament"].unique()
# # find different tournaments using .unique method
# num_unique_tournament = len(unique_tournament)
# # use len to count the unique values
# print(f"Number of unique tournaments: {num_unique_tournament}")

# matches_per_tournament = df.groupby("tournament").size()
# # groupby to group dataframe to tournament and use size to count the rows
# matches_per_tournament_sorted = matches_per_tournament.sort_values(ascending=False)
# # sort values ascending false puts largest tournament at the top
# print(matches_per_tournament_sorted)

# print(df["home_team"].value_counts())
# # Brazil 600 home
# print(df["away_team"].value_counts())
# # Uruguay 565
# print(df["home_team"].max())
# print(df["away_team"].max())
# Aland Islands
# print(df["home_team"].min())
# print(df["away_team"].min())
# Abkhazia

# most_reported_home_team = df["home_team"].value_counts().idxmax()
# # value counts the occurance of the team and idxmax/min returns the count
# most_reported_away_team = df["away_team"].value_counts().idxmax()
# print(most_reported_home_team)
# print(most_reported_away_team)

# least_reported_home_team = df["home_team"].value_counts().idxmin()
# least_reported_away_team = df["away_team"].value_counts().idxmin()
# print(least_reported_home_team)
# print(least_reported_away_team)

# england_home = df["home_team"].value_counts().get("England")
# # value counts home teams  .get to return englands count
# print(england_home)

# england_home_tour = df[df["home_team"]== "England"]
# # telling the dataframe to only find home team england
# england_tournament = england_home_tour.groupby("tournament").size()
# # groupby groups the filtered dataframe by specified tournament then size to count
# print (england_tournament)

# england_home_score = df[df["home_team"]== "England"]
# # filter dataframe only for england
# england_mean_score = england_home_score["home_score"].mean()
# # variable is filtered only for england, find mean from home score
# print (england_mean_score)

# england_home_score = df[df["home_team"]=="England"]
# england_home_score_mean = england_home_score["home_score"].mean()
# print(england_home_score_mean)
# england_above_mean = england_home_score[england_home_score["home_score"] > england_home_score_mean]
# # home score greater than mean
# count_above_mean = england_above_mean.shape[0]
# # shape counts the rows where the condition above was true
# print(count_above_mean)


# england_away_score = df[df["away_team"]=="England"]
# england_away_score_mean = england_away_score["away_score"].mean()
# # print (england_away_score_mean)
# england_above_mean = england_away_score[england_away_score["away_score"] > england_away_score_mean]
# count_above_mean = england_above_mean.shape[0]
# print (count_above_mean)

# home_team_avg = df.groupby("country")["home_score"].mean()
# # groupby to select dataframe by country and calculate home score average
# print(home_team_avg)

# away_team_avg = df.groupby("country")["away_score"].mean()
# print(away_team_avg)

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