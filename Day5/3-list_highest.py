marks_list=input("Enter the list of student marks with spaces: ").split()

highest=int(marks_list[0])
for mark in marks_list:
    mark=int(mark)
    if (mark>highest):
        highest=mark
    print(f"Mark: {mark} highest: {highest}")

print(f"The highest mark is: {highest}")

# You can just use print(max(marks_list))