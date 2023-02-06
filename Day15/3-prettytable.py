from prettytable import PrettyTable
table=PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charamander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])

# example of attribute
table.align='l'
print(table)