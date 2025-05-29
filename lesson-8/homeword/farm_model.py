
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        print(f"{self.name} the {self.species} is eating.")

    def sleep(self):
        print(f"{self.name} the {self.species} is sleeping.")

    def make_sound(self):
        print(f"{self.name} makes a sound.")

    def __str__(self):
        return f"{self.species} named {self.name}, Age: {self.age}"

class Cow(Animal):
    def __init__(self, name, age, milk_production):
        super().__init__(name, age, "Cow")
        self.milk_production = milk_production  

    def graze(self):
        print(f"{self.name} the Cow is grazing in the field.")

    def make_sound(self):
        print(f"{self.name} says Moo!")
class Chicken(Animal):
    def __init__(self, name, age, egg_count):
        super().__init__(name, age, "Chicken")
        self.egg_count = egg_count

    def lay_egg(self):
        self.egg_count += 1
        print(f"{self.name} laid an egg! Total eggs: {self.egg_count}")

    def make_sound(self):
        print(f"{self.name} says Cluck!")

class Sheep(Animal):
    def __init__(self, name, age, wool_amount):
        super().__init__(name, age, "Sheep")
        self.wool_amount = wool_amount  

    def shear(self):
        print(f"{self.name} has been sheared! Collected {self.wool_amount} kg of wool.")
        self.wool_amount = 0

    def make_sound(self):
        print(f"{self.name} says Baa!")

class Farm:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Added {animal} to the farm.")

    def feed_all(self):
        print("\nFeeding all animals...")
        for animal in self.animals:
            animal.eat()

    def animal_sounds(self):
        print("\nAll animals are making sounds...")
        for animal in self.animals:
            animal.make_sound()

    def report(self):
        print("\nFarm Report:")
        for animal in self.animals:
            print(animal)


if __name__ == "__main__":
    cow1 = Cow("Bessie", 5, 20)
    chicken1 = Chicken("Chickpea", 2, 5)
    sheep1 = Sheep("Wooly", 3, 4)
    my_farm = Farm()
    my_farm.add_animal(cow1)
    my_farm.add_animal(chicken1)
    my_farm.add_animal(sheep1)
    my_farm.feed_all()
    my_farm.animal_sounds()

    cow1.graze()
    chicken1.lay_egg()
    sheep1.shear()

    my_farm.report()
