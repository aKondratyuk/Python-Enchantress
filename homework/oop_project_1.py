import random
import math


HOUSES = []
AVAILABLE_DISCOUNTS = [5, 10, 25, 40]


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # Start capital in $
        self.money = 1000

        # At the start, person can't have a house
        self.house = None


class Human(Person):
    def about_me(self):
        print(f"Hello guys! My name is {self.name} and I'm {self.age} years old.")
        print("My dream is buying a big house for my future family!")

    def make_money(self):
        self.money += 128

    def buy_house(self, house):
        if self.money >= house.cost:

            # Deleting house from list of available houses for purchase
            HOUSES.remove(house)
            self.money -= house.cost
            print(f"Greetings!!! {self.name} bought awesome house with price {house.cost}$ and area {house.area}m2")
        else:
            raise Exception(f"Uh... It's seems that you don't have enough money to buy this house. "
                            f"You need {house.cost - self.money}$ more")


class House:
    def __new__(cls, *args, **kwargs):
        obj = super(House, cls).__new__(cls)
        HOUSES.append(obj)
        print(f"House with area {args[0]}m2 and cost {args[1]}$ added to database")
        return obj

    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        if area >= 40:
            self._area = area
        else:
            raise Exception("Area of house cannot be lower than 40 m2")

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, cost):
        if cost >= 40000:
            self._cost = cost
        else:
            raise Exception("Cost of house cannot be lower than 40 000$")

    def apply_purchase_discount(self, discount_percentage):
        self.cost *= (100 - discount_percentage) / 100
        return self.cost


# meta class for Singleton of Realtor class
class RealtorMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Realtor(metaclass=RealtorMetaClass):
    def __init__(self, name):
        self.name = name
        self.houses = HOUSES

    def show_houses(self):
        for i, house in enumerate(HOUSES):
            print(f"House #{i} with area {house.area}m2 costs {house.cost}$")

    def give_discount(self, house):
        random_discount = random.choice(AVAILABLE_DISCOUNTS)

        if len(HOUSES) >= 1:
            house.apply_purchase_discount(random_discount)
            print(f"Nice! You get discount in {random_discount}%")
        else:
            raise Exception("Sorry, but there are no more available houses for purchase.")

    def steal_money(self, human):
        numbers = [num for num in range(0, 10)]
        guess_num = random.choice(numbers)
        random_number = random.choice(numbers)
        if guess_num == random_number:
            # Realtor steals a half of money
            human.money /= 2
            print(f"*Realtor put his hand in your pocket and stole {human.money}$*")
            return True
        else:
            return False


if __name__ == '__main__':
    SIMULATION = True
    while SIMULATION:
        realtor = Realtor("Anna")

        house_1 = House(45, 50000)
        house_2 = House(50, 60000)
        house_3 = House(100, 120000)

        name = input("\n\nHi! Enter your name: ")
        age = int(input("What's your age: "))
        neighbor = Human(name, age)

        print("\nLet's present ourselves\n")
        neighbor.about_me()
        print(f"\nYou have {neighbor.money}$ for the start")
        print("You can earn 128$ per day")
        print(f"\n{realtor.name}: Hello, {neighbor.name}! I'm realtor in this city. I see you wanna buy house")
        print("Look what houses are available for purchase:\n")
        realtor.show_houses()
        print("\n\nWhich house you want to buy?")
        dream_house = int(input("Enter a number of house you want: "))
        money_goal = HOUSES[dream_house].cost
        num_work_days = math.ceil(money_goal / 128)
        print("Today is a pretty day to start making some money $_$")
        print("________________________________________________________")
        print(f"{neighbor.name} went to work at school as a math teacher. A hour rate is 16$ and work day is 8h.")
        for day in range(num_work_days):
            neighbor.make_money()
        print(f"\nYou have been working for {num_work_days} days and you have {neighbor.money}$ now")
        print("Anna: Oh, you come back to buy a house? Today is your lucky day.")
        realtor.give_discount(HOUSES[dream_house])
        if realtor.steal_money(neighbor):
            print("Oh no! It seems that realtor was an aphorist and stole you money")
        else:
            neighbor.buy_house(HOUSES[dream_house])

        SIMULATION = False



