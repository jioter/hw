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
sys.path.append(r"C:\Users\hr\Desktop\it\courses\cursor\base_last_06.07.19\python-course-alphabet\objects_and_classes\homework")
from constants import *
import yaml
from io import StringIO


class Car:
    YAMLTag = u'!Car'

    def __init__(self, price=None, car_type=None, producer=None, number=None, mileage=None, ref=None):
        self.update(price, car_type, producer, number, mileage, ref)

    def update(self, price, car_type, producer, number, mileage, ref=None):
        self.price = price
        self.car_type = car_type
        self.producer = producer
        self.number = number
        self.mileage = mileage
        self._ref = ref

    def price(self, p):
        if not isinstance(p, float):
            raise Exception("Value should be float")
        self._price = p

    def car_type(self, d):
        if d not in CARS_TYPES:
            raise Exception("Unsupported car type")
        self._car_type = d

    def producer(self, v):
        if v not in CARS_PRODUCER:
            raise Exception("Unsupported producer")
        self._producer = v

    def number(self, z):
        self.z = uuid.uuid4()
        self._number = z

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

    def change_number(self, new_value=uuid.uuid4()):
        self.number = new_value
        return self.number

    def toDict(self):
        return dict(price=self.price,
                    car_type=self.car_type,
                    number=self.number,
                    producer=self.producer,
                    mileage=self.mileage,)

    def __repr__(self):
        return f"Car price = {self.price}, " \
            f"car type = {self.car_type}, " \
            f"car number = {self.number}, " \
            f"producer = {self.producer}, " \
            f"mileage = {self.mileage} km"

    @staticmethod
    def to_yaml(dumper, data):
        return dumper.represent_mapping(data.YAMLTag, data.toDict())

    @staticmethod
    def from_yaml(loader, node):
        value = Car()
        yield value
        node_map = loader.construct_mapping(node, deep=True)
        value.update(**node_map)

    def update_self_ref(self, ref):
        self._ref = ref

yaml.add_representer(Car, Car.to_yaml, Dumper=yaml.SafeDumper)
yaml.add_constructor(Car.YAMLTag, Car.from_yaml, Loader=yaml.SafeLoader)


car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)

car1.update_self_ref(car1)

buf = StringIO()
yaml.safe_dump(car1, buf)

yaml_str = buf.getvalue()
print(yaml_str)


data = yaml.safe_load(yaml_str)
# print(data)
# print(id(data), id(data._ref))

with open('to_yaml.yaml', 'w') as ya:
    yaml_dumped = yaml.safe_dump(car1, ya)
    # print(yaml_dumped)

with open('to_yaml.yaml', 'r') as ya:
    yaml_restored = yaml.safe_load(ya)
    print(yaml_restored)
