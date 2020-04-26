import unittest
from objects import Car, Garage, Collectioner
import uuid
import constants


class CarInitTest(unittest.TestCase):

    def test_car_price(self):
        car = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        self.assertIsInstance(car.price, float, msg="Price value should be float")
        self.assertGreater(car.price, 0, msg="Negative value")

    def test_car_type(self):
        car = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        actual = car._car_type
        expected = "Sedan"
        self.assertEqual(actual, expected, msg="Invalid car type")

    def test_car_producer(self):
        car = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        actual = car._producer
        expected = "BENTLEY"
        self.assertEqual(actual, expected, msg="Invalid car type")

    def test_producer_exception_raise(self):
        with self.assertRaises(ValueError, msg="Ups should raise error") as context:
            Car(200.32, "Sedan", "Wrong_producer", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        self.assertTrue("Incorrect car producer" in context.exception.args)
        self.fail()

    def test_car_number(self):
        car = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        actual = car._number
        expected = "47af87f3-3a96-422f-b357-237e4b3684a9"
        self.assertEqual(actual, expected, msg="Invalid car number, should be uuid")

    def test_car_mileage(self):
        car = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        self.assertIsInstance(car.mileage, float, msg="Mileage value should be float")
        self.assertGreater(car.mileage, 0, msg="Negative value")

    def test_car_change_number(self):
        car = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        current_number = car.number
        car.change_number()
        changed_number = car.number
        self.assertNotEqual(current_number, changed_number)


class TestCarStr(unittest.TestCase):
    def test_str(self):
        car = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        actual = str(car)
        expected = f"Car price = 200.32, " \
            f"car type = Sedan, " \
            f"car number = 47af87f3-3a96-422f-b357-237e4b3684a9, " \
            f"producer = BENTLEY, " \
            f"mileage = 50000.0 km"
        self.assertEqual(actual, expected)


class TestComparison(unittest.TestCase):
    def test_equal(self):
        car1 = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        self.assertEqual(car1.price, car2.price)

    def test_less_then(self):
        car1 = Car(100.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        self.assertLess(car1.price, car2.price)

    def test_less_then_equal(self):
        car1 = Car(100.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car3 = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        self.assertLess(car1.price, car2.price)
        self.assertLessEqual(car3.price, car2.price)

    def test_greater_then(self):
        car1 = Car(100.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        self.assertGreater(car2.price, car1.price)

    def test_greater_then_equal(self):
        car1 = Car(100.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car3 = Car(200.32, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        self.assertGreaterEqual(car2.price, car1.price)
        self.assertGreaterEqual(car2.price, car3.price)


class TestGarageInit(unittest.TestCase):
    def test_garage_town(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        garage1 = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        expected = "Amsterdam"
        actual = garage1.town
        self.assertEqual(actual, expected, msg=f"Town should be one of {constants.CARS_TYPES}")

    def test_garage_cars(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        garage1 = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        expected = [car1, car2]
        actual = garage1.cars
        self.assertEqual(actual, expected)

    def test_raise_error_town(self):
        with self.assertRaises(ValueError, msg="Ups should raise error") as context:
            car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
            car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
            garage = Garage("MISTAKE", 3, [car1, car2], uuid.uuid4())
            self.assertTrue("Incorrect garage town" in context.exception.args)
            self.fail()

    def test_places(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        garage = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        expected = 3
        actual = garage.places
        self.assertEqual(actual, expected)
        self.assertIsInstance(actual, int)

    def test_owner(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        garage = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        self.assertIsInstance(garage.owner, uuid.UUID)

    def test_str(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        garage = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        actual = str(garage)
        expected = "Town = Amsterdam " \
                   "Cars:" \
                   "[200.5, 'Sedan', 'BENTLEY', '47af87f3-3a96-422f-b357-237e4b3684a9', 50000.0]" \
                   "[250.4, 'Truck', 'BMW', '47af87f3-3a96-422f-b357-237e4b3684a9', 20000.0]" \
                   "Maximum places in garage = 3" \
                   "Garage owner = c5929fab-7c54-4f51-8ffc-23cb389c197c"
        self.assertEqual(actual, expected)


class TestGarageFunctionality(unittest.TestCase):
    def test_add_car(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        car3 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        garage = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        garage.add_car(car3)
        actual = len(garage.cars)
        expected = 3
        self.assertEqual(actual, expected)

    def test_add_first_car(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        garage = Garage("Amsterdam", 3, [], uuid.uuid4())
        garage.add_car(car1)
        actual = garage.cars
        expected = [car1]
        self.assertEqual(actual, expected)

    def test_remove_car(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        garage = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        garage.remove_car(car2)
        actual = len(garage.cars)
        expected = 1
        self.assertEqual(actual, expected)

    def test_hit_hat(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        car3 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        garage = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        garage.add_car(car3)
        actual = len(garage.cars)
        expected = 3
        self.assertEqual(actual, expected)


class TestCollectionerInit(unittest.TestCase):
    def test_name(self):
        collectioner = Collectioner("Tom", uuid.uuid4(), [])
        actual = collectioner.name
        expected = "Tom"
        self.assertEqual(actual, expected)
        self.assertIsInstance(actual, str)

    def test_register_id(self):
        collectioner = Collectioner("Tom", uuid.uuid4(), [])
        self.assertIsInstance(collectioner.register_id, uuid.UUID)


class TestCollectionerMethods(unittest.TestCase):
    def test_hit_hat(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        car3 = Car(400.60, "Van", "Bugatti", "47af87f3-3a96-422f-b357-237e4b3684a9", 10000.00)
        car4 = Car(500.90, "Sedan", "Buick", "47af87f3-3a96-422f-b357-237e4b3684a9", 70000.00)
        garage1 = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        garage2 = Garage("Kiev", 3, [car3, car4], uuid.uuid4())
        Tom = Collectioner("Tom", uuid.uuid4(), [garage1, garage2])
        actual = Tom.hit_hat
        expected = 1302.40
        self.assertEqual(actual, expected)

    def test_count_garages(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        garage1 = Garage("Amsterdam", 3, [car1], uuid.uuid4())
        Tom = Collectioner("Tom", uuid.uuid4(), [garage1])
        Ralf = Collectioner("Tom", uuid.uuid4(), [])
        self.assertEqual(Tom.garages_count, 3)
        self.assertEqual(Ralf.garages_count, 1)

    def test_car_count(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        car3 = Car(400.60, "Van", "Bugatti", "47af87f3-3a96-422f-b357-237e4b3684a9", 10000.00)
        car4 = Car(500.90, "Sedan", "Buick", "47af87f3-3a96-422f-b357-237e4b3684a9", 70000.00)
        garage1 = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        garage2 = Garage("Kiev", 3, [car3, car4], uuid.uuid4())
        Tom = Collectioner("Tom", uuid.uuid4(), [garage1, garage2])
        actual = Tom.cars_count
        expected = 4
        self.assertEqual(actual, expected)

    def test_add_car(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        car3 = Car(400.60, "Van", "Bugatti", "47af87f3-3a96-422f-b357-237e4b3684a9", 10000.00)
        car4 = Car(500.90, "Sedan", "Buick", "47af87f3-3a96-422f-b357-237e4b3684a9", 70000.00)
        garage1 = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        garage2 = Garage("Kiev", 3, [car3], uuid.uuid4())
        Tom = Collectioner("Tom", uuid.uuid4(), [garage1, garage2])
        Tom.add_car(car4)
        actual = Tom.cars_count
        expected = 4
        self.assertEqual(actual, expected)

    def test_add_car_no_free_places(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        car3 = Car(400.60, "Van", "Bugatti", "47af87f3-3a96-422f-b357-237e4b3684a9", 10000.00)
        car4 = Car(500.90, "Sedan", "Buick", "47af87f3-3a96-422f-b357-237e4b3684a9", 70000.00)
        garage1 = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        garage2 = Garage("Kiev", 3, [car3], uuid.uuid4())
        Tom = Collectioner("Tom", uuid.uuid4(), [garage1, garage2])
        with self.assertRaises(ValueError, msg="Should raise error") as context:
            Tom.add_car(car4)
        self.assertTrue('There are no free places in the specified garage' in context.exception.args)


class TestCollectionerComparison(unittest.TestCase):
    def test_less_equal_then(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(250.40, "Truck", "BMW", "47af87f3-3a96-422f-b357-237e4b3684a9", 20000.00)
        car3 = Car(400.60, "Van", "Bugatti", "47af87f3-3a96-422f-b357-237e4b3684a9", 10000.00)
        car4 = Car(500.90, "Sedan", "Buick", "47af87f3-3a96-422f-b357-237e4b3684a9", 70000.00)
        garage1 = Garage("Amsterdam", 3, [car1, car2], uuid.uuid4())
        garage2 = Garage("Kiev", 3, [car3, car4], uuid.uuid4())
        Tom = Collectioner("Tom", uuid.uuid4(), [garage1])
        Denny = Collectioner("Tom", uuid.uuid4(), [garage1])
        Jerom = Collectioner("Jerom", uuid.uuid4(), [garage2])
        actual_Tom = Tom.hit_hat
        actual_Denny = Denny.hit_hat
        actual_Jerom = Jerom.hit_hat
        expected_Tom = 450.90
        expected_Jerom = 901.50
        self.assertEqual(actual_Tom, expected_Tom)
        self.assertEqual(actual_Jerom, expected_Jerom)
        self.assertLess(actual_Tom, actual_Jerom)
        self.assertLessEqual(actual_Tom, actual_Denny)

    def test_greater_then(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(400.60, "Van", "Bugatti", "47af87f3-3a96-422f-b357-237e4b3684a9", 10000.00)
        garage1 = Garage("Amsterdam", 3, [car1], uuid.uuid4())
        garage2 = Garage("Kiev", 3, [car2], uuid.uuid4())
        Tom = Collectioner("Tom", uuid.uuid4(), [garage1])
        Jerom = Collectioner("Jerom", uuid.uuid4(), [garage2])
        actual_Tom = Tom.hit_hat
        actual_Jerom = Jerom.hit_hat
        self.assertGreater(actual_Tom, actual_Jerom)

    def test_greater_equal_then(self):
        car1 = Car(200.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(400.60, "Van", "Bugatti", "47af87f3-3a96-422f-b357-237e4b3684a9", 10000.00)
        garage1 = Garage("Amsterdam", 3, [car1], uuid.uuid4())
        garage2 = Garage("Kiev", 3, [car2], uuid.uuid4())
        Tom   = Collectioner("Tom", uuid.uuid4(), [garage1])
        Teddy = Collectioner("Teddy", uuid.uuid4(), [garage1])
        Jerom = Collectioner("Jerom", uuid.uuid4(), [garage2])
        actual_Tom = Tom.hit_hat
        actual_Teddy = Teddy.hit_hat
        actual_Jerom = Jerom.hit_hat
        self.assertGreater(actual_Tom, actual_Jerom)
        self.assertGreaterEqual(actual_Tom, actual_Teddy)

    def test_equal(self):
        car1 = Car(400.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        car2 = Car(400.50, "Van", "Bugatti", "47af87f3-3a96-422f-b357-237e4b3684a9", 10000.00)
        garage1 = Garage("Amsterdam", 3, [car1], uuid.uuid4())
        garage2 = Garage("Kiev", 3, [car2], uuid.uuid4())
        Tom   = Collectioner("Tom", uuid.uuid4(), [garage1])
        Teddy = Collectioner("Teddy", uuid.uuid4(), [garage2])
        actual_Tom = Tom.hit_hat
        actual_Teddy = Teddy.hit_hat
        self.assertEqual(actual_Tom, actual_Teddy)

class TestCollectionerOutput(unittest.TestCase):
    def test_str(self):
        car1 = Car(400.50, "Sedan", "BENTLEY", "47af87f3-3a96-422f-b357-237e4b3684a9", 50000.00)
        garage1 = Garage("Amsterdam", 3, [car1], uuid.uuid4())
        Tom = Collectioner("Tom", uuid.uuid4(), [garage1])
        actual = str(Tom)
        expected = """ Name = Tom 
                    Garages & cars: 
                    ['Amsterdam', 3, 200.5, 'Sedan', 'BENTLEY', '47af87f3-3a96-422f-b357-237e4b3684a9', 50000.0, UUID('4f36a82b-599f-4378-b0e8-5c57d324e15b')] 
                    Garage owner = b7549015-ccaa-4b6d-afa7-0751cf176caa"""
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()

