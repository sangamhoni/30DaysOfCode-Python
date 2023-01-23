# WAP to add the digits of a two digit number

two_digit_number = input("Type a two digit number: ")

sum= int(two_digit_number) // 10
two_digit_number= int(two_digit_number) % 10
sum= sum + (two_digit_number)
print(sum)