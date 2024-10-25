import matplotlib.pyplot as plt

# years = [2018, 2019, 2020, 2021, 2022, 2023]
# python_position = [7, 4, 4, 3, 4, 3]
# js_position = [1, 1, 1, 1, 1, 1]
# sql_position = [4,3,3,4,3,4]
# typescript_position = [12,10,9,7,5,5]

# plt.plot(years, python_position, label="Python")
# plt.plot(years, js_position, label="JavaScript", linestyle="--")
# plt.plot(years, sql_position, label="SQL", linestyle="-.")
# plt.plot(years, typescript_position, label="TypeScript", linestyle=":")
# # x axis first, then y
# plt.title("Most wanted language ranking")
# plt.xlabel("Year")
# plt.ylabel("Position")
# plt.ylim(bottom = 15, top = 0)
# # sets limits of axis
# # plt.legend(["Python","Java", "SQL", "TypeScript"])
# plt.legend()
# plt.show()

# Activity 1

Days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

Youtube_pos = [2,1,3,6,3]
Twitter_pos = [1,1,0,0,2]
Whatsapp_pos = [3,1,0,2,1]
Raid_pos = [0,4,2,3,3]
Tiktok_pos = [3,0,1,0,2]

plt.plot(Days, Youtube_pos, label="Youtube", linestyle="-", color="red", marker="*")
plt.plot(Days, Twitter_pos, label="Twitter", linestyle="--", color="blue", marker="o", linewidth=3)
plt.plot(Days, Whatsapp_pos, label="Whatsapp", linestyle="-.", color="green", marker="^")
plt.plot(Days, Raid_pos, label="Raid", linestyle=":", color="purple", marker="x", linewidth=2)
plt.plot(Days, Tiktok_pos, label="Tiktok", linestyle="--", color="black", marker="+")
plt.title("App Useage Time")
plt.xlabel("Day of the week")
plt.ylabel("Hours spent")
plt.ylim(bottom=0, top=8)
plt.legend()
plt.grid()
plt.show()