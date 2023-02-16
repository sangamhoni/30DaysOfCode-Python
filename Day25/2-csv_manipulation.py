import csv

temperature=[]

with open('./weather-data.csv', mode='r') as data_file:
    data = csv.reader(data_file)
    for row in data:
        temp=row[1]
        if temp.isdigit():
            temperature.append(temp)

    # print(data)

print(temperature)
