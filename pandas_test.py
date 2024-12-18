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

planet = (["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"])
temperature = ([167, 464, 15, -65, -110, -140, -195, -200])
radius = ([2440, 6052, 6371, 3390, 69911, 58232, 25362, 24622])
colour = (["Grey", "Golden Brown", "Blue", "Red", "Yellow Brown Red", "Yellow Brown Grey", "Cyan", "Blue"])
interesting_feat = (["Not too hot for ice", "Moonless", "Habbitual", "Thicker atmosphere in the past", "Comet catcher", "Has rings", "Very Stormy", "Supersonic Winds"])

planets_Df = pd.DataFrame({"Planet" : planet, 
                           "Temp (C)" : temperature, 
                           "Radius (km)" : radius, 
                           "Colour" : colour,
                            "Interesting Fact" : interesting_feat})

planets_Df.columns = ["Planet", "Temp (C)", "Radius (km)", "Colour", "Interesting Fact"]

planets_Df["Discovered"] = ["Thomas Harriet", "Galileo", "Humans", "Galileo", "Galileo", "Galileo", "William Herschel", "Johann Galle"]
planets_Df["Year Discovered"] = [1610, 1610, 0, 1610, 1610, 1610, 1787, 1880]
planets_Df["Elements"] = ["Nickel", "Carbon Dioxide", "Nitrogen", "Carbon Dioxide", "Hydrogen", "Hydrogen", "Methane", "Helium"]

new_planet = pd.DataFrame({"Planet":["Pluto"], 
                           "Temp (C)" : [-232],
                            "Radius (km)"  : [1188], 
                            "Colour": ["Red"], 
                            "Interesting Fact" : ["Dwarf Planet"],
                             "Discovered": ["Clyd Tombaugh"],
                              "Year Discovered" : [1930], 
                              "Elements" : ["Nitrogen"]})
planets_Df = pd.concat([planets_Df,new_planet], ignore_index=True)
# print(planets_Df)
# planets_Df.to_excel("Planets_DF.xlsx", index=False)
# print(planets_Df.loc[1:4])
planets_Df = planets_Df.set_index("Planet")
user_input = input("What planet would you like to know more about?: ")
if user_input in planets_Df.index:
    print(f"Great! Lets explore {user_input}!")
    print("'Planet' -- 'Temp (C)' -- 'Radius (km)' -- 'Colour' -- 'Interesting Fact'")
    specific_column = input("Please type in one of these for more information, or type 'all' for everything: ")
    if specific_column == "all":
        print(planets_Df.loc[user_input])
    elif specific_column in planets_Df.columns:    
        print(f"{specific_column} for {user_input}: {planets_Df.at[user_input, specific_column]}")
else:
    print("Not found in Database")