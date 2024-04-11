import unittest
from Classes.ui import Ui
from Classes.car import Car


class CarRegistryTests(unittest.TestCase):
    def test_add_cars(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_reg_upper(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='EO09 TZD', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_sipp_lower(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='ppbd', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_manufacturer_lower(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='ford', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_seats_edge_case(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=2, width=1234, length=4321, maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_seats_edge_case_max(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=10, width=1234, length=4321, maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_seats_str(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity='2', width=1234, length=4321, maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_width_edge_case(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1000, length=4321, maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_width_edge_case_max(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=2500, length=4321, maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_width_str(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width='1234', length=4321, maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_length_edge_case(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=1000, maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_length_edge_case_max(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=10000, maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_length_str(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length='4321', maximum_speed=123, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_speed_edge_case(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=1, range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_speed_str(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed='123', range_mpg=50)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_range_edge_case(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123, range_mpg=1)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_range_str(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123, range_mpg='50')
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.add_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len+1), end_len)

    def test_add_cars_largest_car_id(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123, range_mpg=50)
        # act
        test_ui.my_car_registry.add_car(test_car)
        # assert
        self.assertEqual(test_car.car_id, Car.largest_car_id)

    def test_remove_cars(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123, range_mpg=50)
        test_ui.my_car_registry.add_car(test_car)
        # act
        start_len = len(test_ui.my_car_registry.cars_list)
        test_ui.my_car_registry.remove_car(test_car)
        end_len = len(test_ui.my_car_registry.cars_list)
        # assert
        self.assertEqual((start_len - 1), end_len)

    def test_remove_cars_largest_car_id(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123, range_mpg=50)
        # act
        test_ui.my_car_registry.add_car(test_car)
        test_ui.my_car_registry.remove_car(test_car)
        # assert
        self.assertNotEqual(test_car.car_id, Car.largest_car_id)

    def test_return_car_to_garage(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123, range_mpg=50, on_hire=True)
        test_ui.my_car_registry.add_car(test_car)
        # act
        test_ui.my_car_registry.return_car_to_garage(test_car.car_id)
        # assert
        self.assertEqual(test_car.on_hire, False)

    def test_hire_out(self):
        # arrange
        Car.largest_car_id = 0
        test_ui = Ui()
        test_car = Car(registration_plate='eo09 tzd', sipp_code='PPBD', manufacturer='FORD', model_type='FORDCAR',
                       maximum_seat_capacity=5, width=1234, length=4321, maximum_speed=123, range_mpg=50)
        test_ui.my_car_registry.add_car(test_car)
        # act
        test_ui.my_car_registry.hire_out(test_car.car_id)
        # assert
        self.assertEqual(test_car.on_hire, True)


if __name__ == '__main__':
    unittest.main()
