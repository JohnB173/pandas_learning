import pandas as pd

languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
ranking = pd.Series([3,1,2,4])

df = pd.DataFrame({"Languages" : languages,
                   "Ranking" : ranking})
print(df)