import csv

with open("weather.csv", "r") as f:
    data = list(csv.reader(f))

city = input("Enter a city: ")

for row in data:
    if row[0] == city:
        print(row[1])