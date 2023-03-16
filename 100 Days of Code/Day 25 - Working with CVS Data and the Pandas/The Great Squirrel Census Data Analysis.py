"""
Yeni bir dosya oluştur. (squirrel_count) Dosyanın içine rengine göre kaç tane sincp olduğunu ekle
"""

import pandas


# fur_color = data.PrimaryFurColor
#
# gray = []
# cinnamon = []
# black = []
# white = []
#
# for i in fur_color:
#     if i == "Black":
#         black.append(i)
#     if i == "White":
#         white.append(i)
#     if i == "Gray":
#         gray.append(i)
#     else:
#         cinnamon.append(i)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray = len(data[data["PrimaryFurColor"] == "Gray"])
white = len(data[data["PrimaryFurColor"] == "White"])
cinnamon = len(data[data["PrimaryFurColor"] == "Cinnamon"])
black = len(data[data["PrimaryFurColor"] == "Black"])

fur_dict = {
    "Color": ["Gray", "Black", "White", "Cinnamon"],
    "Count": [gray, black, white, cinnamon]
}
data = pandas.DataFrame(fur_dict)
data.to_csv("squirrel_count")
