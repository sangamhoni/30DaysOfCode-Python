import pandas

data=pandas.read_csv('./weather-data.csv')

# converting to a dictionary {}
data_dict= data.to_dict()

# converting a column to a list []
temp_list=data['temp'].to_list()

# to get mean of the temperature column
average= sum(temp_list) / len(temp_list)
# print(round(average, 1))
# OR 
# print(data['temp'].mean())

# getting data in columns
# print(data['condition'])
# # OR
# print(data.condition)

# get data in a row
# print(data[data.day == 'Monday'])
# # prints the first row with the day attribute Monday