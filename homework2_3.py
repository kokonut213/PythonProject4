class Animal:
    def __init__(self,name):
        self.name=name
    def make_sound(self):
        return "animal sound"
    def get_name(self):
        return self.name

class Dog(Animal):
    def __init__(self,name,breed):
     super().__init__(name)
     self.breed=breed
    def make_sound(self):
        return"woof,woof"
    def get_breed(self):
        return self.breed

class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color=color

    def make_sound(self):
        return"meow"

    def get_color(self):
        return self.color

    def purr(self):  # Thêm hàm mới
        return "purrrrrr"



animal = Animal("Generic animal")
dog = Dog(name="Buddy",breed="Husky")
cat = Cat(name="Kitty",color="White")

animals = [animal,dog,cat]
for pet in animals:
     print(f"{pet.get_name()},says:{pet.make_sound()}")
     print(f"{dog.get_name()} is a:{dog.get_breed()}")
     print(f"{cat.get_name()} is {cat.get_color()}")
     print(f"{cat.get_name()} also: {cat.purr()}")  # Gọi hàm mới
