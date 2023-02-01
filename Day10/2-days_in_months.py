# WAP to find whether a given year is leap year or not

def is_leapyear(year):
    if (year%4==0):
        if (year%100==0):
            if (year%400==0):
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    days_per_month=[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (month==2):
        if (is_leapyear(year)==True):
            return days_per_month[1]+1
        else:
            return days_per_month[1]
    return days_per_month[month-1]


year=int(input("Enter a year: "))
month=int(input("Enter a month: "))
days=days_in_month(year, month)
print (days)

