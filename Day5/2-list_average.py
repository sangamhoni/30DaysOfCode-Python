number_list=input("Enter the list of numbers: ").split()

sum=0
total=0
for number in number_list:
    sum=sum+int(number_list[total])
    total+=1

print(f"The average is: {round(sum/total, 2)}")

# You can just use len(number_list) and sum(number_list)