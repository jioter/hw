import uuid
from constants import *

"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
    price - значення типу float. Всі ціни за дефолтом в одній валюті.
    type - одне з перечисленних значеннь з CARS_TYPES в docs.
    producer - одне з перечисленних значеннь в CARS_PRODUCER.
    number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
    mileage - значення типу float. Пробіг автомобіля в кілометрах.


    Автомобілі можна перівнювати між собою за ціною.
    При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

    Автомобіль має метод заміни номеру.
    номер повинен відповідати UUID

Гараж має наступні характеристики:
   + town - одне з перечислених значеннь в TOWNS
   + cars - список з усіх автомобілів які знаходяться в гаражі
   + places - значення типу int. Максимально допустима кількість автомобілів в гаражі
   + owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

+

    add(car) -> Добавляє машину в гараж, якщо є вільні місця
    remove(cat) -> Забирає машину з гаражу.
    hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
    name - значення типу str. Його ім'я
    garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
    register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
    hit_hat() - повертає ціну всіх його автомобілів.
    garages_count() - вертає кількість гаріжів.
    сars_count() - вертає кількість машиню
    add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
    Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""


# class Collectioner:
#     sum_cars_number = 0
#     def __init__(self, name, garages = 0, register_id):
#         self.name = name
#         self.garages = garages
#         self.register_id = register_id
#
#     def hit_hat(self):
#         return Car.price # add what to summarize. all cars price

#     def garages_count(self):
#         return sum(Garages) # sum garages
#     def add_car(self):
#         add # To complete
class Car:
    def __init__(self, price, car_type, producer, number, mileage):
        self.price = price
        self.car_type = car_type
        self.producer = producer
        self.number = number
        self.mileage = mileage

    @property
    def price(self):
        # print(self._price)
        return self._price

    @price.setter
    def price(self, p):
        if not isinstance(p, float):
            raise Exception("Value should be float")
        self._price = p    # need to set currency?

    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, d):
        if d not in CARS_TYPES:
            raise Exception("Unsupported car type")
        self._car_type = d

    @property
    def producer(self):
        return self._producer

    @producer.setter
    def producer(self, v):
        if v not in CARS_PRODUCER:
            raise Exception("Unsupported producer")
        self._producer = v

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, z):
        self.z = uuid.uuid4()
        self._number = z

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, r):
        if not isinstance(r, float):
            raise Exception("Value should be float")
        self._mileage = r  # in km?

    def __cmp__(self, other):
        return Car.price, other.price

    def __lt__(self, other):
        return Car.price < other.price

    def __gt__(self, other):
        return Car.price > other.price

    def __ge__(self, other):
        return Car.price >= other.price

    def __le__(self, other):
        return Car.price <= other.price

    def __eq__(self, other):
        return Car.price == other.price

    def logs(self):
        attributes = [attr for attr in dir(Car) if not attr.startswith('__')]
        return print(attributes)

    def __str__(self):
        return f"Car price = {self.price}, " \
            f"car type = {self.car_type}, " \
            f"car number = {self.number}, " \
            f"producer = {self.producer}, " \
            f"mileage = {self.mileage} km"

    def change_number(self, new_value=uuid.uuid4()):
        self.number = new_value
        return self.number


class Garage:
    # https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
    # like this also not works
    def __init__(self, town, places, cars=None, owner=None):
        self.town = town
        if cars is None:
            cars = []
        self.cars = cars
        self.places = places
        self.owner = owner

    @property
    def town(self):
        return self._town

    @town.setter
    def town(self, p):
        if p not in TOWNS:
            raise Exception("Town doesn't exist")
        self._town = p

    def cars(self):
        self.cars = self.cars.append(self.cars)
        return self.cars  # mb list of cars from class Cars

    @property
    def places(self):
        return self._places

    @places.setter
    def places(self, p,):
        if not isinstance(p, int):
            raise Exception("Value should be int")
        self._places = p

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, p):
        if not isinstance(p, uuid.UUID):
            raise Exception("Value should be UUID")
        self._owner = p

    def __str__(self):
        get_car_attr = [[
            getattr(self.cars[z], 'price'),
            getattr(self.cars[z], 'car_type'),
            getattr(self.cars[z], 'producer'),
            getattr(self.cars[z], 'number'),
            getattr(self.cars[z], 'mileage')]
            for z in range(len(self.cars))]

        print_car_attr = '\n '.join([str(row) for row in get_car_attr])

        return f" Town = {self.town}, \n " \
            f" Cars: \n" \
            f" {print_car_attr} \n" \
            f" Places in garage = {self.places} \n" \
            f" Garage owner = {self.owner}"

    def add_car(self, new_car):
        if len(self.cars) <= self.places:
            self.cars.append(new_car)  # check if it works right
        else:
            print("There is no free places left.")

    def remove_car(self, old_car):
        self.cars.remove(old_car)

    def hit_hat(self):
        return sum(Car.price) # how correct


car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
car2 = Car(300.50, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
car3 = Car(300.50, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 10000.00)
car4 = Car(300.50, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 70000.00)

print(car1.price < car2.price)

car1.logs()

print(str(car1))
print(str(car2))

car1.change_number()
# print(str(car1))

garage1 = Garage("Amsterdam", 5, [car1, car2, car3, car4], uuid.uuid4())
print(str(garage1))

