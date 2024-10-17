import pandas as pd
import numpy as np

df = pd.read_excel("dev_rankings.xlsx")
df = df.set_index("Languages")
print(df)
