def calculate(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        # add, multiply
        print(value)
        # 3. 9

calculate(add=3, multiply=9)

#

def calculate1(n, **kwargs):
    n+=kwargs['add']
    n+=kwargs['multiply']
    print(n)
    # 25 output

calculate1(2, add=3, multiply=9)

#

class Car:
    def __init__(self, **kw):
        # self.make=kw['make']
        # self.model=kw["model"]
        # or
        self.make=kw.get('make')
        self.model=kw.get("model")
        # this method is preferred since it doesnt throw error if there's not all variables while calling the class

my_car=Car(make="Nissan", model="GT=R")
print(my_car.make)
print(my_car.model)

my_car=Car(make="Nissan")
print(my_car.make)
print(my_car.model)
# this shows error if we do: self.model=kw["model"]
# if we do: self.model=kw.get("model"), if prints None
