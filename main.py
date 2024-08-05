# with open("weather_data.csv") as weather_data_file:
#     data = weather_data_file.readlines()
#     print(data)
#


# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# Make variable data and assign it to the csv file
data = pandas.read_csv("weather_data.csv")

# Make CSV sa a dictionary
data_dict = data.to_dict()
print(data_dict)

# get a max value from the temp column
print(data["temp"].max())


# Get avaerage value from the temp column
print(data["temp"].mean())

# Get data in columns
print(data["condition"])

# Get max data value form column
print(data[data.temp == data.temp.max()])


#Get Monday temp data convert with Fahrenheit
monday = data[data.day == "Monday"]
print(monday.temp * (9/5) + 32)


#Create a dataframe from scratch


data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")


vadsr = input("enter")