import pandas

sq_data=pandas.read_csv('./squirrel_data.csv')

fur_data=sq_data['Primary Fur Color']

gray_squirrels=sq_data[sq_data['Primary Fur Color']=='Gray']
gray_count=len(gray_squirrels)

cinnamon_squirrels=sq_data[sq_data['Primary Fur Color']=='Cinnamon']
cinnamon_count=len(cinnamon_squirrels)

black_squirrels=sq_data[sq_data['Primary Fur Color']=='Black']
black_count=len(black_squirrels)

data_dict={
    'Fur Color': ['Gray', 'Cinnamon', 'Black'],
    'Count': [gray_count, cinnamon_count, black_count]
}

furcolor_data=pandas.DataFrame(data_dict)
furcolor_data.to_csv('./squirrel_count.csv')
