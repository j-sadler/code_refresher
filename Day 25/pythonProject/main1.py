# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temps = []
#     for row in data:
#         if row[1] != "temp":
#             print(row[1])
#
#             temps.append(int(row[1]))
#     print(temps)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirls = data[data["Primary Fur Color"] == "Gray"]
print(len(gray_squirls))
primary_colors = ["Gray, Cinnamon, Black"]
primary_color_count = {"Fur Color": [], "Count": []}

for color in primary_colors:
    primary_color_count["Fur Color"].append(color)

    color_count = len(data[data["Primary Fur Color"] == color])
    print(color_count)

print(primary_color_count["Fur Color"])
print(primary_color_count)



