"""
Для попереднього домашнього завдання.
Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) файлу відповідно

Для класів Колекціонер Машина і Гараж написати методи, які зберігають стан обєкту в файли формату
yaml, json, pickle відповідно.

Для класів Колекціонер Машина і Гараж написати методи, які конвертують обєкт в строку формату
yaml, json, pickle відповідно.

Для класу Колекціонер Машина і Гараж написати методи, які створюють інстанс обєкту
з (yaml, json, pickle) строки відповідно


Advanced
Добавити опрацьовку формату ini

"""

import uuid
import sys
sys.path.append("C:/Users/hr/Desktop/cursor/base_last_06.07.19/python-course-alphabet/objects_and_classes/homework")
from constants import *
import json
import pickle

"""
Вам небхідно написати 3 класи. Колекціонери Гаражі та Автомобілі.
Звязкок наступний один колекціонер може мати багато гаражів.
В одному гаражі може знаходитися багато автомобілів.

Автомобіль має наступні характеристики:
   + price - значення типу float. Всі ціни за дефолтом в одній валюті.
   + type - одне з перечисленних значеннь з CARS_TYPES в docs.
   + producer - одне з перечисленних значеннь в CARS_PRODUCER.
   + number - значення типу UUID. Присвоюється автоматично при створенні автомобілю.
   + mileage - значення типу float. Пробіг автомобіля в кілометрах.


   + Автомобілі можна перівнювати між собою за ціною.
   + При виводі(logs, print) автомобілю повинні зазначатися всі його атрибути.

   + Автомобіль має метод заміни номеру.
   + номер повинен відповідати UUID

Гараж має наступні характеристики:
   + town - одне з перечислених значеннь в TOWNS
   + cars - список з усіх автомобілів які знаходяться в гаражі
   + places - значення типу int. Максимально допустима кількість автомобілів в гаражі
   + owner - значення типу UUID. За дефолтом None.


Повинен мати реалізованими наступні методи:
    + add(car) -> Добавляє машину в гараж, якщо є вільні місця
    + remove(car) -> Забирає машину з гаражу.
    + hit_hat() -> Вертає сумарну вартість всіх машин в гаражі


Колекціонер має наступні характеристики
  + name - значення типу str. Його ім'я
  + garages - список з усіх гаражів які належать цьому Колекціонеру. Кількість гаражів за замовчуванням - 0
  + register_id - UUID; Унікальна айдішка Колекціонера.

    Повинні бути реалізовані наступні методи:
  + hit_hat() - повертає ціну всіх його автомобілів.
  + garages_count() - вертає кількість гаріжів.
  + сars_count() - вертає кількість машин.
  + add_car() - додає машину у вибраний гараж. Якщо гараж не вказаний, то додає в гараж, де найбільше вільних місць.
  + Якщо вільних місць немає повинне вивести повідомлення про це.

    Колекціонерів можна порівнювати за ціною всіх їх автомобілів.
"""


class Collectioner:

    def __init__(self, name, register_id, garages=None):
        self.name = name
        if garages is None:
            garages = []
        self.garages = garages
        self.register_id = register_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        if not isinstance(n, str):
            raise Exception("Value should be str")
        self._name = n

    @property
    def register_id(self):
        return self._register_id

    @register_id.setter
    def register_id(self, p):
        # if not isinstance(p, uuid.UUID):
        #     raise Exception("Value should be UUID")
        self._register_id = None

    def garages(self):
        self.garages = self.garages.append(self.garages)
        return self.garages

    def __str__(self):
        get_garages_attr = [[
            getattr(self.garages[z], 'town'),
            getattr(self.garages[z], 'places'),
            Car.__getattribute__(getattr(self.garages[z], 'cars')[c], 'price'),
            Car.__getattribute__(getattr(self.garages[z], 'cars')[c], 'car_type'),
            Car.__getattribute__(getattr(self.garages[z], 'cars')[c], 'producer'),
            Car.__getattribute__(getattr(self.garages[z], 'cars')[c], 'number'),
            Car.__getattribute__(getattr(self.garages[z], 'cars')[c], 'mileage'),
            getattr(self.garages[z], 'owner')]
            for z in range(len(self.garages))
            for c in range(len(getattr(self.garages[z], 'cars')))]

        print_garages_attr = '\n '.join([str(row) for row in get_garages_attr])

        return f" Name = {self.name} \n " \
            f" Garages & cars: \n" \
            f" {print_garages_attr} \n" \
            f" Garage owner = {self.register_id}"

    def hit_hat(self):
        car_price_sum = [sum(Car.__getattribute__(getattr(self.garages[z], 'cars')[c], 'price')
                             for z in range(len(self.garages))
                             for c in range(len(getattr(self.garages[z], 'cars'))))]
        print(f" Total price of all {self.name} cars =", car_price_sum[0])
        return car_price_sum[0]

    def garages_count(self):
        print(" Number of Garages =", len(self.garages))

    def cars_count(self):
        rez = [getattr(self.garages[z], 'cars') for z in range(len(self.garages))]
        print(" Number of cars =", sum(len(i) for i in rez))

    def add_car(self, some_car, garage=None):
        if garage is not None:
            if garage in self.garages:
                index = self.garages.index(garage)
                self.garages[index].add_car(some_car)
        else:
            rez = [len(getattr(self.garages[z], 'cars')) for z in range(len(self.garages))]
            rez2 = [getattr(self.garages[z], 'places') for z in range(len(self.garages))]

            diff = []
            for i in rez2:
                for j in rez:
                    diff.append(i - j)
            empty_positions = diff[::len(rez) + 1]
            if not any(empty_positions):
                print('There is no free space left in all garages of current collectioner.')

            highest_empty_space = max(empty_positions)
            index_of_HES = empty_positions.index(highest_empty_space)
            self.garages[index_of_HES].add_car(some_car)

    def __cmp__(self, other):
        return Collectioner.hit_hat(self), other.hit_hat()

    def __lt__(self, other):
        if Collectioner.hit_hat(self) < other.hit_hat():
            print(f" {other.name} total car price is greater by", other.hit_hat() - Collectioner.hit_hat(self))
        if other.hit_hat() < Collectioner.hit_hat(self):
            print(f" {self.name} total car price is greater by", Collectioner.hit_hat(self) - other.hit_hat())

    def __gt__(self, other):
        if Collectioner.hit_hat(self) > other.hit_hat():
            print(f" {self.name} total car price is greater by", Collectioner.hit_hat(self) - other.hit_hat())
        elif other.hit_hat() > Collectioner.hit_hat(self):
            print(f" {other.name} total car price is greater by", other.hit_hat() - Collectioner.hit_hat(self))

    def __ge__(self, other):
        if Collectioner.hit_hat(self) >= other.hit_hat():
            print(f" {self.name} total car price is greater by", Collectioner.hit_hat(self) - other.hit_hat())
        elif other.hit_hat() >= Collectioner.hit_hat(self):
            print(f" {other.name} total car price is greater by", other.hit_hat() - Collectioner.hit_hat(self))

    def __le__(self, other):
        if Collectioner.hit_hat(self) <= other.hit_hat():
            print(f" {other.name} total car price is greater by", other.hit_hat() - Collectioner.hit_hat(self))
        if other.hit_hat() <= Collectioner.hit_hat(self):
            print(f" {self.name} total car price is greater by", Collectioner.hit_hat(self) - other.hit_hat())

    def __eq__(self, other):
        if Collectioner.hit_hat(self) == other.hit_hat():
            print(f" Total car price of both collectioners is equal")

    @classmethod
    def from_json(cls, data):
        name = data['name']
        register_id = data['register_id']
        garages = json.loads(data['garages'], object_hook=Garage.from_json)
        obj = Collectioner(name=name, register_id=register_id, garages=garages)
        return obj

    @staticmethod
    def to_json(obj):
        garages = json.dumps(obj.garages, default=Garage.to_json)
        data = {"name": obj.name, "register_id": obj.register_id, "garages": garages}
        return data

    def json_serialize_to_string(self):
        return json.dumps(self, default=Collectioner.to_json, indent=4)

    @staticmethod
    def json_deserialize_from_string(obj):
        return json.loads(obj, object_hook=Collectioner.from_json)

    def json_serialize_to_file(self, json_file):
        with open(json_file, 'w') as file:
            return json.dump(self, file, default=Collectioner.to_json, indent=4)

    @staticmethod
    def json_deserialize_from_file(json_file):
        with open(json_file, 'r') as file:
            return json.load(file, object_hook=Collectioner.from_json)

    def pickle_serialize_to_string(self):
        return pickle.dumps(self)

    @staticmethod
    def pickle_deserialize_from_string(obj):
        return pickle.loads(obj)

    def pickle_serialize_to_file(self, pickle_file):
        with open(pickle_file, mode='wb') as pick:
            return pickle.dump(self, pick)

    @staticmethod
    def pickle_deserialize_from_file(pickle_file):
        with open(pickle_file, 'rb') as f:
            return pickle.load(f)


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
        if not isinstance(p, float):
            raise Exception("Value should be float")
        self._price = p

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
        self._mileage = r

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

    @classmethod
    def from_json(cls, data):
        price = data['price']
        car_type = data['car_type']
        producer = data['producer']
        number = data['number']
        mileage = data['mileage']
        obj = Car(price=price, car_type=car_type, producer=producer, number=number, mileage=mileage)
        return obj

    @staticmethod
    def to_json(obj):
        data = {"price": obj.price, "car_type": obj.car_type, "producer": obj.producer,
                "number": obj.number, "mileage": obj.mileage}
        return data

    def json_serialize_to_string(self):
        return json.dumps(self, default=Car.to_json)

    @staticmethod
    def json_deserialize_from_string(obj):
        return json.loads(obj, object_hook=Car.from_json)

    def json_serialize_to_file(self, json_file):
        with open(json_file, 'w') as file:
            json.dump(self, file, default=Car.to_json, indent=4)

    @staticmethod
    def json_deserialize_from_file(json_file):
        with open(json_file, 'r') as file:
            return json.load(file, object_hook=Car.from_json)

    def pickle_serialize_to_string(self):
        return pickle.dumps(self)

    @staticmethod
    def pickle_deserialize_from_string(obj):
        return pickle.loads(obj)

    def pickle_serialize_to_file(self, pickle_file):
        with open(pickle_file, mode='wb') as pick:
            return pickle.dump(self, pick)

    @staticmethod
    def pickle_deserialize_from_file(pickle_file):
        with open(pickle_file, 'rb') as f:
            return pickle.load(f)


class Garage:
    # https://www.toptal.com/python/python-class-attributes-an-overly-thorough-guide
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
        return self.cars

    @property
    def places(self):
        return self._places

    @places.setter
    def places(self, p, ):
        if not isinstance(p, int):
            raise Exception("Value should be int")
        self._places = p

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, p):
        # if not isinstance(p, uuid.UUID):
        #     raise Exception("Value should be UUID")
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

        return f" Town = {self.town} \n " \
            f" Cars: \n" \
            f" {print_car_attr} \n" \
            f" Maximum places in garage = {self.places} \n" \
            f" Garage owner = {self.owner}"

    def add_car(self, new_car):
        if len(self.cars) < self.places:
            self.cars.append(new_car)
        else:
            # raise Exception(ValueError, "no places")
            print("There is no free places left in Garage.")

    def remove_car(self, old_car):
        self.cars.remove(old_car)

    def hit_hat(self):
        print("Number of cars in Garage = ", len(self.cars))

    @classmethod
    def from_json(cls, data):
        town = data['town']
        places = data['places']
        cars = json.loads(data['cars'], object_hook=Car.from_json)
        owner = data['owner']
        obj = Garage(town=town, places=places, cars=cars, owner=owner)
        return obj

    @staticmethod
    def to_json(obj):
        cars = json.dumps(obj.cars, default=Car.to_json)
        data = {"town": obj.town, "places": obj.places, "cars": cars,
                "owner": obj.owner}
        return data

    def json_serialize_to_string(self):
        return json.dumps(self, default=Garage.to_json, indent=4)

    def json_deserialize_from_string(obj):
        return json.loads(obj, object_hook=Garage.from_json)

    def json_serialize_to_file(self, json_file):
        with open(json_file, 'w') as file:
            return json.dump(self, file, default=Garage.to_json, indent=4)

    @staticmethod
    def json_deserialize_from_file(json_file):
        with open(json_file, 'r') as file:
            return json.load(file, object_hook=Garage.from_json)

    def pickle_serialize_to_string(self):
        return pickle.dumps(self)

    @staticmethod
    def pickle_deserialize_from_string(obj):
        return pickle.loads(obj)

    def pickle_serialize_to_file(self, pickle_file):
        with open(pickle_file, mode='wb') as pick:
            return pickle.dump(self, pick)

    @staticmethod
    def pickle_deserialize_from_file(pickle_file):
        with open(pickle_file, 'rb') as f:
            return pickle.load(f)


# /////// self-TEST class Car///////

car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
car3 = Car(400.60, "Van", "Bugatti", "47af87f3-3a96-422f-b357-237e4b3684a9", 10000.00)
car4 = Car(500.90, "Sedan", "Buick", "47af87f3-3a96-422f-b357-237e4b3684a9", 70000.00)
car5 = Car(600.20, "Wagon", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 33000.00)
car6 = Car(600.20, "Wagon", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 33000.00)
car7 = Car(600.20, "Wagon", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 33000.00)
car8 = Car(600.20, "Wagon", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 33000.00)

# print(car1.price < car2.price)

# car1.logs()

# print(str(car1))
# print(str(car2))

# car1.change_number()
# print(str(car1))

# /////// self-TEST class Garage ///////

garage1 = Garage("Amsterdam", 3, [car1, car2], "8b793cac-b92b-41bf-a3cc-71b54b00b624")
garage2 = Garage("Kiev", 3, [car3, car4], "8b793cac-b92b-41bf-a3cc-71b54b00b624")
garage3 = Garage("Rome", 3, [car5, car6], uuid.uuid4())
garage4 = Garage("London", 4, [car7, car8], uuid.uuid4())

# check cars limit in garage
# garage1.add_car(car5)
# garage1.add_car(car6)
# garage1.add_car(car7)

# print(str(garage1))

# garage1.remove_car(car5)
# print(str(garage1))

# garage1.hit_hat()  # sum of cars in garage

# /////// self-TEST class Collectioner ///////

Tom = Collectioner("Tom", register_id="8b793cac-b92b-41bf-a3cc-71b54b00b624", garages=[garage1, garage2])
David = Collectioner("David", uuid.uuid4(), [garage3, garage4])
# print(str(David))
# print(Tom > David)
# Tom.garages_count()
# Tom.cars_count()
# Tom.add_car(garage2, car8)
# Tom.add_car(car8)

