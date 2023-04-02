# learning args

def add(*args):
    sum=0
    for n in args:
        sum+=n
    return n

numbers=(input("Enter the numbers separated my comma: "))
number=numbers.split(", " or " " or ",")
print(number)


# 1. Adding arguments without any value in a function
def add(a=1, b=2):
    print(a+b)

# here, the default values for a and b will be 1 and 2 if no arguments are given
add()
add(3, 5)

# 2. unlimited arguments
def multiply(*args):
    multiple=1
    for n in args:
        multiple*=n
    return multiple

for i in range(5):
    numbers=input("All numbers: ")
    print(multiply(numbers))
