WATER=300
MILK=200
COFFEE=100
EARNINGS=0

def enough_resources(water, milk, coffee):
    '''to check if there's enough milk, coffee and water'''
    global WATER, MILK, COFFEE  
    if (water>WATER):
        print("Sorry, there is not enough water.")
        return False
    elif (milk>MILK):
        print("Sorry, there is not enough milk.")
        return False
    elif (coffee>COFFEE):
        print("Sorry, there is not enough coffee.")
        return False
    else:
        return True
    
def enough_money(price):
    '''to check if the user has enough money'''
    print("Please insert coins.")
    quarter=int(input("How many quarters? "))
    dime=int(input("How many dimes? "))
    nickel=int(input("How many nickels? "))
    penny=int(input("How many pennies? "))
    
    total_money=quarter*0.25 + dime*0.1 + nickel*.05 + penny*.01
    if (total_money>=price):
        print(f"Here is ${round(total_money-price, 2)} in change.")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def kitchen_update (water, milk, coffee, money, drink):
    '''to update the resources after the coffee is made'''
    global WATER, MILK, COFFEE, EARNINGS
    WATER-=water
    MILK-=milk
    COFFEE-=coffee
    EARNINGS+=money
    print(f"Here is your {drink}. Enjoy!")


# MAIN PROGRAM
def coffee_machine():
    order=input("What would you like? (espresso/latte/cappuccino): ").lower()

    if (order=='espresso'):
        if enough_resources(water=50, milk=0, coffee=18):
            if enough_money(1.5):
                kitchen_update(water=50, milk=0, coffee=18, money=1.5, drink="espresso")

    elif (order=='latte'):
        if enough_resources(water=200, milk=150, coffee=24):
            if enough_money(2.5):
                kitchen_update(water=200, milk=150, coffee=24, money=2.5, drink="latte")

    elif(order=='cappuccino'):
        if enough_resources(water=250, milk=100, coffee=24):
            if enough_money(3):
                kitchen_update(water=250, milk=100, coffee=24, money=3, drink="cappuccino")

    elif order=='report':
        print(f" Water: {WATER} \n Milk: {MILK} \n Coffee: {COFFEE} \n Money: ${EARNINGS}")
        
    elif order=='off':
        print("Turning machine off...")
        exit()

    else:
        print("\n Today's Summary: ")
        print(f" Water: {WATER} \n Milk: {MILK} \n Coffee: {COFFEE} \n Money: ${EARNINGS}")
        exit()

    coffee_machine()


coffee_machine()