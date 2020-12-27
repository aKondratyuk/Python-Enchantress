class Animal:
    def __init__(self, animal_type, speed):
        self.animal_type = animal_type
        self.speed = speed

    def run(self):
        return self.animal_type + " has speed of running " + self.speed


class Dog(Animal):
    def __init__(self, animal_type, speed):
        super().__init__(animal_type, speed)
        self.sound = "Haf-haf"


class Cat(Animal):
    def __init__(self, animal_type, speed):
        super().__init__(animal_type, speed)
        self.sound = "Meow-meow"


class Bird(Animal):
    def __init__(self, animal_type, speed):
        super().__init__(animal_type, speed)
        self.sound = "Chick-chirick"


class Cow(Animal):
    def __init__(self, animal_type, speed):
        super().__init__(animal_type, speed)
        self.sound = "Mooo-mooo"


class Horse(Animal):
    def __init__(self, animal_type, speed):
        super().__init__(animal_type, speed)
        self.sound = "Igo-go"


if __name__ == '__main__':

    my_animals = [Dog("Dog", "48 km/h"),
                  Cat("Cat", "48 km/h"),
                  Bird("Bird", "241 km/h"),
                  Cow("Cow", "40 km/h"),
                  Horse("Horse", "88 km/h")]

    for animal in my_animals:
        print(animal.sound + "\n" + animal.run() + "\n")
