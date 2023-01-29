def prime_checker(n):
    divisor=0
    for checker in range(2, n):
        if (n %checker==0):
            divisor+=1
    if (divisor != 0):
        print("Not a prime number")
    else:
        print("A prime number")

number=int(input("Check your number hereL: "))
prime_checker(n=number)
        