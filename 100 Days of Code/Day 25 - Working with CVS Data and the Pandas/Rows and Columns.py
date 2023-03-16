#
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for i in data:
#         if i[1] != "temp":
#             temperature.append(i[1])
#     print(temperature)

import pandas

"""
The two primary data structures of pandas, Series1 (1-dimensional) and DataFrame (2-dimensional),
hande the vast majority of typical use cases in finance, statics social science and many areas of engineering. 

Every single sheet inside an Excel file or inside a Google sheet file would be considered a DataFrame in Pandas.

Series is basically equivalent to a list. Its like a one column in table.
"""
data = pandas.read_csv("weather_data.csv")
print(data["temp"])
print(type(data))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
#
# # Finding avarage of column
# print(data["temp"].mean())
#
# # Finding max value of column
# print(data["temp"].max())
#
# # Get data in columns
# print(data["condition"])
# print(data.condition)
# #
# # Get data in row
# print(data[data.day == "Monday"])  # -> Monday    12     Sunny
# print(data[data.temp == data.temp.max()]) # Get max temp in row
#
# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# print(monday_temp * 9/5 + 32) #converting Celcius to Fahrenheit
#
# # Create a dataframe from stracth
# data_dict = {
#     "students": ["Amy", "James", "Angele"],
#     "scores": [76,56,65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")