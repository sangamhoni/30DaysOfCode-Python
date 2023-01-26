# WAP to place the treasure 'X' on the destined location using coordinates of columns, rows

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? (column rows): ")
column=int(position[0])
row=int(position[-1])

if (row==1):
    row1[column-1]="X "
elif (row==2):
    row2[column-1]="X "
else:
    row3[column-1]="X "
    

print(f"{row1}\n{row2}\n{row3}")