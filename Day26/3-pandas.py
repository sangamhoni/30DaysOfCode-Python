import pandas

weather_data=pandas.read_csv('./weather-data.csv')

# print(weather_data)

# print data of a row
# print(weather_data[weather_data.day=='Wednesday'])

# to print the row with max temperature
# print(weather_data[weather_data.temp==weather_data.temp.max()])

# to convert monday's temperature into fahrehheit from celsius
monday_data =(weather_data[weather_data.day=='Monday'])
monday_temp = int(monday_data.temp)
print(monday_temp * 9 / 5 + 32)

# creating data_frame from scratch
data_dict={
    'students': ['Amy', 'James', 'Angela'],
    'scores': [76, 56, 65]
}
    # this converts the dictionary into a dataframe
data=pandas.DataFrame(data_dict)
    # this saves the dataframe in the harddrive as 'new_data.csv'
data.to_csv('./new_data.csv')



