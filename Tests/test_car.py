import unittest
from Classes.car import Car
from Classes.invalidinput import (InvalidManufacturer, InvalidRegistration, InvalidSIPPCode, InvalidSeatNum,
                                  InvalidWidth, InvalidLength, InvalidModel, InvalidSpeed, InvalidRange)


class CarTests(unittest.TestCase):
    def test_incorrect_reg(self):
        # assert
        with self.assertRaises(InvalidRegistration):
            test_car = Car(registration_plate='bad registration', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_reg_int(self):
        # assert
        with self.assertRaises(InvalidRegistration):
            test_car = Car(registration_plate=12, sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_sipp(self):
        # assert
        with self.assertRaises(InvalidSIPPCode):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='AAAA', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_sipp_int(self):
        # assert
        with self.assertRaises(InvalidSIPPCode):
            test_car = Car(registration_plate='eo09 tzd', sipp_code=1234, manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_manufacturer(self):
        # assert
        with self.assertRaises(InvalidManufacturer):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='vroomvroom',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_manufacturer_int(self):
        # assert
        with self.assertRaises(InvalidManufacturer):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer=1234,
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_model_int(self):
        # assert
        with self.assertRaises(InvalidModel):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type=1234, maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_seats_min(self):
        # assert
        with self.assertRaises(InvalidSeatNum):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=1, width=1234, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_seats_max(self):
        # assert
        with self.assertRaises(InvalidSeatNum):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=11, width=1234, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_seats_neg(self):
        # assert
        with self.assertRaises(InvalidSeatNum):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=-1, width=1234, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_seats_float(self):
        # assert
        with self.assertRaises(InvalidSeatNum):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5.5, width=1234, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_width_min(self):
        # assert
        with self.assertRaises(InvalidWidth):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=999, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_width_max(self):
        # assert
        with self.assertRaises(InvalidWidth):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=2501, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_width_neg(self):
        # assert
        with self.assertRaises(InvalidWidth):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=-1, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_width_float(self):
        # assert
        with self.assertRaises(InvalidWidth):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234.56, length=4321, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_length_min(self):
        # assert
        with self.assertRaises(InvalidLength):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=999, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_length_max(self):
        # assert
        with self.assertRaises(InvalidLength):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=10001, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_length_neg(self):
        # assert
        with self.assertRaises(InvalidLength):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=-1, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_length_float(self):
        # assert
        with self.assertRaises(InvalidLength):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=6543.21, maximum_speed=123,
                           range_mpg=50)

    def test_incorrect_speed_neg(self):
        # assert
        with self.assertRaises(InvalidSpeed):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=-1,
                           range_mpg=50)

    def test_incorrect_speed_str(self):
        # assert
        with self.assertRaises(InvalidSpeed):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=4321, maximum_speed='str',
                           range_mpg=50)

    def test_incorrect_range_neg(self):
        # assert
        with self.assertRaises(InvalidRange):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123,
                           range_mpg=-1)

    def test_incorrect_range_str(self):
        # assert
        with self.assertRaises(InvalidRange):
            test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD',
                           model_type='FORDCAR', maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123,
                           range_mpg='aaaa')


if __name__ == '__main__':
    unittest.main()
