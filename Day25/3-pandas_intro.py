import pandas

data=pandas.read_csv('./weather-data.csv')

# prints the column with the 'temp' value in the first row
# print(data['temp'])

# print(data)

# converting to a dictionary {}
data_dict= data.to_dict()
# print(data_dict)

# converting a column to a list []
temp_list=data['temp'].to_list()
# print(temp_list)

# to get mean of the temperature column
average= sum(temp_list) / len(temp_list)
# print(round(average, 1))

# using pandas to get average
# print(data['temp'].mean())

# to get max temp value
# print(data['temp'].max())

# getting data in columns
# print(data['condition'])
# # OR
# print(data.condition)

# get data in a row
# print(data[data.day == 'Monday'])
# # prints the first row with the day attribute Monday