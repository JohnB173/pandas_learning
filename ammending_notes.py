import pandas as pd

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
ranking = pd.Series([3,1,2,4])

df = pd.DataFrame({"Languages" : languages,
                   "Ranking" : ranking})
# df.loc[4] = ["PHP", 11]
# df.loc[3.5] = ["KESL", 20]

# df = df.sort_index()
# df = df.reset_index(drop=True)

new_data = pd.DataFrame({"Languages": ["PHP", "TypeScript", "Java"],
                         "Ranking": [11, 5, 7],
                         })

df = pd.concat([df,new_data], ignore_index=True)
# print(df)

# new_languages = pd.DataFrame({"Languages": ["Java","TypeScript"],
#                               "Ranking": [7, 5]})
# df = pd.concat([df,new_languages], ignore_index=True)

df["Ranking 2022"] = [4,1,2,3,10,6,5]
df["Ranking 2020"] = [4,1,2,3,8,9,5]
df["Ranking 2019"] = [4,1,2,3,8,10,5]

df.insert(3, "Ranking 2021",[3,1,2,4,11,5,7] )
df.rename(columns={"Ranking": "Ranking 2023"}, inplace=True)
df = df.set_index("Languages")
# print(df["Ranking 2019"])
# print(df[["Ranking 2020", "Ranking 2019"]])
# print(df.loc["HTML"])
# print(df.loc[:, "Ranking 2020"])
# print(df)
# print(df.loc["Python":"HTML":1,"Ranking 2023":"Ranking 2019":2])
# print(df.iloc[3])
# print(df.at["HTML", "Ranking 2023"])
print(df.head(2))