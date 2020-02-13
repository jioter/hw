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

    town - одне з перечислениз значеннь в TOWNS
    cars - список з усіх автомобілів які знаходяться в гаражі
    places - значення типу int. Максимально допустима кількість автомобілів в гаражі
    owner - значення типу UUID. За дефолтом None.


    Повинен мати реалізованими наступні методи

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


class Collectioner:
    def __init__(self, name, garages = 0, register_id):
        self.name = name
        self.garages = garages
        self.register_id = register_id

    def hit_hat(self):
        return sum(Car.self.price) # add what to summarize. all cars price
    def garages_count(self):
        return sum(Garages) # sum garages
    def add_car(self):
        add # To complete
class Car:
    def __init__(self, price, car_type, producer, number, mileage):
        self.price = price
        self.car_type = car_type
        self.producer = producer
        self.number = number
        self.mileage = mileage

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, p):
        if not isinstance(p, float): raise Exception("Value should be float")
        self._price = p # need to set currency?

    @property
    def car_type(self):
        return self._car_type

    @car_type.setter
    def car_type(self, d):
        if not d in CARS_TYPES: raise Exception("Unsupported car type")
        self._car_type = d

    @property
    def producer(self):
        return self._producer

    @producer.setter
    def producer(self, v):
        if not v in CARS_PRODUCER: raise Exception("Unsupported producer")
        self._producer = v

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, z): # why not used, how to set default value
        z = uuid.uuid4()
        self._number = z

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, r):
        if not isinstance(r, float): raise Exception("Value should be float")
        self._mileage = r # in km?

    def compare(self): # how to implement it
        pass
    def logs(self):
        attributes = [attr for attr in dir(Car) if not attr.startswith('__')]
        return print(attributes)
    def change_number(self):
        number = uuid.uuid4()
        return number

class Garage:
    def __init__(self, town, cars, places, owner = None):
        self.town = town
        self.cars = []
        self.places = places
        self.owner = owner

    @property
    def places(self):
        return self._places

    @places.setter
    def places(self, p):
        if not isinstance(p, int): raise Exception("Value should be int")
        self._places = p

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, p):
        if not isinstance(p, uuid.UUID): raise Exception("Value should be UUID")
        self._owner= p

    def add_car(self, new_car):
        self.Garage.cars.append(new_car) # finish it
    def remove_car(self, old_car):
        self.cars.remove(old_car)
    def hit_hat(self):
        return sum(Car.price) # how correct


