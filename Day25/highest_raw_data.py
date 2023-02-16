import pandas
data=pandas.read_csv('./weather-data.csv')

print(data[data.day=="Monday")