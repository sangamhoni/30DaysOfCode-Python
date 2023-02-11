class Animal:
    def __init__(self):
        self.num_eyes=2
        self.breathe()

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        # does all the 'breathe' methods of the super class and also additional ones added below superclass
        super().breathe()
        print("doing this underwater")

    def swim(self):
        print("moving in water.")



nemo=Fish()
nemo.swim()
print(nemo.num_eyes)