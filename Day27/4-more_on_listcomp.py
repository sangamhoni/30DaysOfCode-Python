# program to see the common numbers in both files

file1_list=[]
file2_list=[]

with open('./4-file1.txt') as file1:
    # print(file1.readlines())
    file1_list=(file1.readlines())
with open('./4-file2.txt') as file2:
    file2_list=(file2.readlines())

# print(file1_list)
# print(file2_list)

common_number=[int(num) for num in file1_list if num in file2_list]
print(common_number)

# the above one-liner is similar to the code below:
# common_number=[]
# for n in range(len(file1_list)):
#     if file1_list[n] in file2_list:
#         common_number.append(file1_list[n])


