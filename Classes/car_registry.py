from Classes.car import Car
from Classes.invalidinput import (InvalidLength, InvalidWidth, InvalidRegistration, InvalidManufacturer, InvalidSeatNum,
                                  InvalidSIPPCode, InvalidModel, InvalidSpeed, InvalidRange, CarOnHire, CarInGarage,
                                  InvalidLinesInDatabase, InvalidCarId, InvalidOnHire)
import re
import time
import os


class CarRegistry:

    def __init__(self, cars=None):
        self.cars_list = []
        script_dir = os.path.dirname(__file__)
        rel_path = "../CarRegistry.dat"
        abs_file_path = os.path.join(script_dir, rel_path)
        if cars is None:
            with open(abs_file_path, 'r') as cars_raw:
                for line in cars_raw:
                    try:
                        if len(re.findall(',', line)) == 10:
                            car_as_list = line.split(',')
                            try:  # verifies if the car has valid input
                                car_obj = Car(car_id=int(car_as_list[0]), registration_plate=car_as_list[1],
                                              manufacturer=car_as_list[2], model_type=car_as_list[3],
                                              sipp_code=car_as_list[4], maximum_seat_capacity=int(car_as_list[5]),
                                              width=int(car_as_list[6]), length=int(car_as_list[7]),
                                              maximum_speed=float(car_as_list[8]), range_mpg=float(car_as_list[9]),
                                              on_hire=car_as_list[10])
                                Car.largest_car_id = car_as_list[0]
                                self.cars_list.append(car_obj)
                            except InvalidCarId:
                                print('Car cannot be added, invalid car ID entered')
                            except InvalidRegistration:
                                print('Car cannot be added, invalid registration entered')
                            except InvalidManufacturer:
                                print('Car cannot be added, invalid manufacturer entered')
                            except InvalidSIPPCode:
                                print('Car cannot be added, invalid SIPP code entered')
                            except InvalidSeatNum:
                                print('Car cannot be added, invalid number of seats entered')
                            except InvalidWidth:
                                print('Car cannot be added, invalid width entered')
                            except InvalidLength:
                                print('Car cannot be added, invalid length entered')
                            except InvalidModel:
                                print('Car cannot be added, invalid model entered')
                            except InvalidSpeed:
                                print('Car cannot be added, invalid speed entered')
                            except InvalidRange:
                                print('Car cannot be added, invalid range (mpg) entered')
                        else:
                            raise InvalidLinesInDatabase
                    except InvalidLinesInDatabase:
                        print('Car cannot be added, invalid line')

    def update_cars(self):  # writing over database with the list of cars
        script_dir = os.path.dirname(__file__)
        rel_path = "../CarRegistry.dat"
        abs_file_path = os.path.join(script_dir, rel_path)
        with open(abs_file_path, 'w') as cars_raw:
            for car_item in self.cars_list:
                new_line = (f"{str(car_item.car_id)},{str(car_item.registration_plate).upper()},"
                            f"{str(car_item.manufacturer).upper()},{str(car_item.model_type).upper()},"
                            f"{str(car_item.sipp_code).upper()},{car_item.maximum_seat_capacity},"
                            f"{round(car_item.width)},{round(car_item.length)},{round(car_item.maximum_speed, 2)},"
                            f"{round(car_item.range_mpg, 2)},{str(car_item.on_hire)}\n")
                cars_raw.write(new_line)

    def add_car(self, new_car):
        try:
            self.cars_list.append(new_car)  # add car to car list
            Car.largest_car_id = new_car.car_id
        except InvalidRegistration:
            print('Car cannot be added, invalid registration entered')  # verifies if the car has valid input
        except InvalidManufacturer:
            print('Car cannot be added, invalid manufacturer entered')
        except InvalidSIPPCode:
            print('Car cannot be added, invalid SIPP code entered')
        except InvalidSeatNum:
            print('Car cannot be added, invalid number of seats entered')
        except InvalidWidth:
            print('Car cannot be added, invalid width entered')
        except InvalidLength:
            print('Car cannot be added, invalid length entered')
        except InvalidModel:
            print('Car cannot be added, invalid model entered')
        except InvalidSpeed:
            print('Car cannot be added, invalid speed entered')
        except InvalidRange:
            print('Car cannot be added, invalid range (mpg) entered')

    def remove_car(self, car_to_remove):
        if Car.largest_car_id == car_to_remove.car_id:
            # decrease the largest car id if car with the largest id is removed
            Car.largest_car_id -= 1
        self.cars_list.remove(car_to_remove)  # remove car from car list

    def return_car_to_garage(self, car_id):
        car_for_garage = None
        t_or_f = None
        for car_item in self.cars_list:
            if car_item.car_id == car_id:
                car_for_garage = car_item
                t_or_f = eval(str(car_for_garage.on_hire))
                break
            else:
                pass
        try:
            if t_or_f is None or car_for_garage is None:
                raise InvalidOnHire
            if not t_or_f:
                raise CarInGarage
            else:
                car_for_garage.on_hire = False
                print(f'Vehicle ID {car_id} is now in the garage!')
                time.sleep(2)
        except CarInGarage:  # error message for car in garage
            print(f'Vehicle ID {car_id} is already in the garage!')
            time.sleep(2)
        except InvalidOnHire:
            print(f'Vehicle ID {car_id} is corrupt/ does not exist.')
            time.sleep(2)

    def hire_out(self, car_id):
        car_for_hire = None
        t_or_f = None
        for car_item in self.cars_list:
            if car_item.car_id == car_id:
                car_for_hire = car_item
                t_or_f = eval(str(car_for_hire.on_hire))
                break
            else:
                pass
        try:
            if t_or_f is None or car_for_hire is None:
                raise InvalidOnHire
            if t_or_f:
                raise CarOnHire
            else:
                car_for_hire.on_hire = True
                print(f'Vehicle ID {car_id} is now on hire!')
                time.sleep(2)
        except CarOnHire:  # error message for car in garage
            print(f'Vehicle ID {car_id} is already on hire!')
            time.sleep(2)
        except InvalidOnHire:
            print(f'Vehicle ID {car_id} is corrupt/ does not exist.')
            time.sleep(2)
