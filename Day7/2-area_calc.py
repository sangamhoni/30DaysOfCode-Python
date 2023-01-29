# WAP to calc how many cans of paint a wall needs to be painted.
# A can of paint covers 5 sq. m of area of wall

def paint_can(height, width):
    area=height*width
    no_of_can+=.5
    no_of_can=round(area/5)
    print(f"You need {no_of_can} cans of paint")

h=int(input("Enter the height of wall: "))
w=int(input("Enter the width of wall:  "))

paint_can(height=h, width=w)


