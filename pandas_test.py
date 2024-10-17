import pandas as pd
import numpy as np

# languages = pd.Series(["Python", "JavaScript", "HTML", "SQL"])
# ranking = pd.Series([3,1,2,4])
# # print(ranking)

# # df = pd.DataFrame([("Anne", 30), ("Bill", 27), ("Charlie", 55)], columns=["Name", "Age"])
# # print(df)

# # df = pd.DataFrame({"Languages" : languages,
# #                    "Ranking" : ranking})
# # print(df)

# df = pd.concat([languages, ranking], axis=1,)
# df.columns = ["Languages", "Ranking"]
# print(df)

# df = pd.read_csv("speeds.csv")
# df = pd.read_excel("speeds.xlsx")
# print(df)

# planets_Df = pd.DataFrame([("Mercury", 167, 2440, "Grey", "Not too hot for ice"), ("Venus", 464, 6052, "Golden Brown", "Moonless"), ("Earth", 15, 6371, "Blue", "Habbitual"), ("Mars", -65, 3390, "Red", "Thicker atmosphere in the past"), ("Jupiter", -110, 69911, "Yellow Brown Red", "Comet Catcher"), ("Saturn", -140, 58232, "Yellow Brown Grey", "Has rings"), ("Uranus", -195, 25362, "Cyan", "Very Stormy"), ("Neptune", -200, 24622, "Blue", "Supersonic Winds")])

# Activity 1

planet = pd.Series(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
temperature = pd.Series([167, 464, 15, -65, -110, -140, -195, -200])
radius = pd.Series([2440, 6052, 6371, 3390, 69911, 58232, 25362, 24622])
colour = pd.Series(["Grey", "Golden Brown", "Blue", "Red", "Yellow Brown Red", "Yellow Brown Grey", "Cyan", "Blue"])
interesting_feat = pd.Series(["Not too hot for ice", "Moonless", "Habbitual", "Thicker atmosphere in the past", "Comet catcher", "Has rings", "Very Stormy", "Supersonic Winds"])

planets_Df = pd.DataFrame([planet, temperature, radius, colour, interesting_feat])
planets_Df = pd.concat([planet, temperature, radius, colour, interesting_feat], axis=1)
planets_Df.columns = ["Planet", "Temp (C)", "Radius (km)", "Colour", "Interesting Fact"]
print(planets_Df)