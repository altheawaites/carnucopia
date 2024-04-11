from Classes.invalidinput import (InvalidManufacturer, InvalidRegistration, InvalidSIPPCode, InvalidSeatNum,
                                  InvalidWidth, InvalidLength, InvalidCarId, InvalidModel, InvalidSpeed, InvalidRange,
                                  InvalidOnHire)
import re


class Car:

    largest_car_id: int = 0

    def __init__(self, registration_plate, sipp_code, manufacturer, model_type, maximum_seat_capacity, width,
                 length, maximum_speed, range_mpg, car_id=None, on_hire=False):
        if car_id is None:
            self._car_id = int(self.largest_car_id) + 1
        elif int(car_id) > int(self.largest_car_id):
            self._car_id = int(car_id)
        else:
            raise InvalidCarId
        exp = (r'(^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$)|(^[A-Z][0-9]{1,3}[A-Z]{3}$)|(^[A-Z]{3}[0-9]{1,3}[A-Z]$)|(^[0-9]'
               r'{1,4}[A-Z]{1,2}$)|(^[0-9]{1,3}[A-Z]{1,3}$)|(^[A-Z]{1,2}[0-9]{1,4}$)|(^[A-Z]{1,3}[0-9]{1,3}$)|(^'
               r'[A-Z]{1,3}[0-9]{1,4}$)|(^[0-9]{3}[DX]{1}[0-9]{3}$)')
        if re.search(exp, str(registration_plate).upper()) is None:
            raise InvalidRegistration
        else:
            self._registration_plate = str(registration_plate)
        exp = r'^[CDEFGHIJOPRSU][BCDFKLPQTVW][ABCDNM][CDEHINQRVZ]$'
        if re.search(exp, str(sipp_code).upper()) is None:
            raise InvalidSIPPCode
        else:
            self._sipp_code = str(sipp_code)
        if str(manufacturer).upper() in ['CHEVROLET', 'CHRYSLER', 'FORD', 'HONDA', 'ISUZU', 'TOYOTA']:
            self._manufacturer = manufacturer
        else:
            raise InvalidManufacturer
        if type(model_type) is str:
            self._model_type = str(model_type)
        else:
            raise InvalidModel
        if str(maximum_seat_capacity).isdigit() and 1 < int(maximum_seat_capacity) <= 10:
            self._maximum_seat_capacity = int(maximum_seat_capacity)
        else:
            raise InvalidSeatNum
        if str(width).isdigit() and 1000 <= int(width) <= 2500:
            self._width = int(width)
        else:
            raise InvalidWidth
        if str(length).isdigit() and 1000 <= int(length) <= 10000:
            self._length = int(length)
        else:
            raise InvalidLength
        try:
            if float(maximum_speed) > 0:
                self._maximum_speed = float(maximum_speed)
            else:
                raise InvalidSpeed
        except ValueError:
            raise InvalidSpeed
        try:
            if float(range_mpg) > 0:
                self._range_mpg = float(range_mpg)
            else:
                raise InvalidRange
        except ValueError:
            raise InvalidRange
        if on_hire in ['TRUE', 'True', 'true', True, 'True\n']:
            self._on_hire = True
        elif on_hire in ['FALSE', 'False', 'false', False, 'False\n']:
            self._on_hire = False
        else:
            raise InvalidOnHire

    def __str__(self):
        line = (f"{str(self.car_id).rjust(2)}  {self.registration_plate.upper().ljust(8)}  "
                f"{self.manufacturer.upper().ljust(12)}  {self.model_type.upper().ljust(8)}  {self.sipp_code.upper()}  "
                f"{str(self.maximum_seat_capacity).rjust(4)}  {str(self.width).rjust(5)}  {str(self.length).rjust(6)}  "
                f"{str('{0:.2f}'.format(float(self.maximum_speed))).rjust(6)}  "
                f"{str('{0:.2f}'.format(float(self.range_mpg))).rjust(5)}  {str(self.on_hire).ljust(8)}")
        return line

    @property
    def car_id(self):
        return self._car_id

    @car_id.setter
    def car_id(self, car_id):
        if car_id is None:
            self._car_id = int(self.largest_car_id) + 1
        elif int(car_id) > int(self.largest_car_id):
            self._car_id = int(car_id)
        else:
            raise InvalidCarId

    @property
    def registration_plate(self):
        return self._registration_plate

    @registration_plate.setter
    def registration_plate(self, reg_plate):
        exp = (r'(^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$)|(^[A-Z][0-9]{1,3}[A-Z]{3}$)|(^[A-Z]{3}[0-9]{1,3}[A-Z]$)|(^[0-9]'
               r'{1,4}[A-Z]{1,2}$)|(^[0-9]{1,3}[A-Z]{1,3}$)|(^[A-Z]{1,2}[0-9]{1,4}$)|(^[A-Z]{1,3}[0-9]{1,3}$)|(^'
               r'[A-Z]{1,3}[0-9]{1,4}$)|(^[0-9]{3}[DX]{1}[0-9]{3}$)')
        if re.search(exp, reg_plate.upper()) is None:
            raise InvalidRegistration
        else:
            self._registration_plate = reg_plate

    @property
    def sipp_code(self):
        return self._sipp_code

    @sipp_code.setter
    def sipp_code(self, sipp):
        exp = r'^[CDEFGHIJOPRSU][BCDFKLPQTVW][ABCDNM][CDEHINQRVZ]$'
        if re.search(exp, sipp.upper()) is None:
            raise InvalidSIPPCode
        else:
            self._sipp_code = sipp

    @property
    def manufacturer(self):
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, man):
        if man.upper() in ['CHEVROLET', 'CHRYSLER', 'FORD', 'HONDA', 'ISUZU', 'TOYOTA']:
            self._manufacturer = man
        else:
            raise InvalidManufacturer

    @property
    def model_type(self):
        return self._model_type

    @model_type.setter
    def model_type(self, model):
        if type(model) is str:
            self._model_type = model
        else:
            raise InvalidModel

    @property
    def maximum_seat_capacity(self):
        return self._maximum_seat_capacity

    @maximum_seat_capacity.setter
    def maximum_seat_capacity(self, seats):
        if str(seats).isdigit() and 1 < int(seats) <= 10:
            self._maximum_seat_capacity = int(seats)
        else:
            raise InvalidSeatNum

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if str(width).isdigit() and 1000 <= int(width) <= 2500:
            self._width = int(width)
        else:
            raise InvalidWidth

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if str(length).isdigit() and 1000 <= int(length) <= 10000:
            self._length = int(length)
        else:
            raise InvalidLength

    @property
    def maximum_speed(self):
        return self._maximum_speed

    @maximum_speed.setter
    def maximum_speed(self, speed):
        try:
            if float(speed) > 0:
                self._maximum_speed = float(speed)
            else:
                raise InvalidSpeed
        except ValueError:
            raise InvalidSpeed

    @property
    def range_mpg(self):
        return self._range_mpg

    @range_mpg.setter
    def range_mpg(self, mpg):
        try:
            if float(mpg) > 0:
                self._range_mpg = float(mpg)
            else:
                raise InvalidRange
        except ValueError:
            raise InvalidRange

    @property
    def on_hire(self):
        return self._on_hire

    @on_hire.setter
    def on_hire(self, value):
        if value in ['TRUE', 'True', 'true', True]:
            self._on_hire = True
        elif value in ['FALSE', 'False', 'false', False]:
            self._on_hire = False
        else:
            raise InvalidOnHire
