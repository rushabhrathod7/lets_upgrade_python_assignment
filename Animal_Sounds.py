class Animal:
    def make_sound(self):
        print("Generic animal sound")

class Dog(Animal):
    def make_sound(self):
        print("Dog: Bark!")

class Cat(Animal):
    def make_sound(self):
        print("Cat: Meow!")

def animal_sound_in_zoo(animal):
    animal.make_sound()

if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    animal_sound_in_zoo(dog)  
    animal_sound_in_zoo(cat)
