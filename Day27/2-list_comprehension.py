# (new_list=[new_item for item in list]

# adds 1 to every number in the 'numbers' list
numbers=[1,2, 3]
new_list=[n+1 for n in numbers]
# print(new_list)

name='Sangam'
letters=[letter for letter in name]
# converts all letters into a list format

list=[i*2 for i in range(1, 5)]
# print(list)


# CONDITIONAL LIST COMPREHENSION
names=['Alex', 'Caroline', 'Dave', 'Eleanor', 'Freddie', 'Beth']
short_names=[name for name in names if len(name)<5]
# print(short_names)

long_names=[name.upper() for name in names if len(name)>4]
print(long_names)
