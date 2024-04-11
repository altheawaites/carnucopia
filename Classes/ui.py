import re
import time
from Classes.car import Car
from Classes.car_registry import CarRegistry
from Classes.invalidinput import ReturnToMenu, InvalidMenuOption


class Ui:

    def __init__(self):
        self.my_car_registry = CarRegistry()
        self.return_to_menu = True

    @staticmethod
    def display_header():
        print('Pos  ID  Reg       Manufacturer  Model     SIPP  Seat  Width  Length   Speed    MPG  On Hire?')

    def display_items(self):
        i = 1
        print_list = []
        for car_item in self.my_car_registry.cars_list:
            item = f"{str(i).rjust(3)}  {Car.__str__(self=car_item)}"
            print_list.append(item)
            i += 1
        for item in print_list:
            print_item = re.sub(r'\n', '', item)
            print(print_item)

    @staticmethod
    def display_menu():
        print('Menu:')
        print('> (A)dd car to car registry')
        print('> (D)elete car from car registry')
        print('> (H)ire out')
        print('> (R)eturn to garage')
        print('> (U)pdate car registry')
        print('')
        print('> e(X)it')
        print('')

    def process_option(self):
        self.return_to_menu = False  # when true process will stop and return to start menu
        choice = input("> ")
        choice = choice.upper()
        try:
            if choice == 'A':  # add car
                self.ui_add_car()
            elif choice == 'D':  # remove/ delete car
                self.ui_remove_car()
            elif choice == 'H':  # hiring a vehicle
                self.ui_hire_out()
            elif choice == 'R':  # returning a vehicle
                self.ui_return_car()
            elif choice == 'U':  # updates CarRegistry.dat database
                self.my_car_registry.update_cars()
                raise ReturnToMenu  # returns to menu
            elif choice == 'X':  # exit
                self.ui_exit()
            else:  # if incorrect option selected
                raise InvalidMenuOption
        except InvalidMenuOption:  # if incorrect option selected, continuing program
            print('Enter an option from the menu!')
            time.sleep(1.5)
            self.return_to_menu = True
        except ReturnToMenu:  # cancel/ finish operation and return to menu
            self.return_to_menu = True

    def ui_add_car(self):
        reg = self.input_reg()
        manufacturer = self.input_manufacturer()
        model = self.input_model()
        sipp = self.input_sipp()
        seating_capacity = self.input_seating_capacity()
        width = self.input_width()
        length = self.input_length()
        max_speed = self.input_speed()
        mpg = self.input_mpg()
        new_car = Car(registration_plate=reg, manufacturer=manufacturer, model_type=model, sipp_code=sipp,
                      maximum_seat_capacity=int(seating_capacity), width=int(width), length=int(length),
                      maximum_speed=float(max_speed), range_mpg=float(mpg))
        self.my_car_registry.add_car(new_car=new_car)  # adds car to list
        raise ReturnToMenu

    @staticmethod
    def input_reg():
        reg = None
        while reg is None:
            input_reg = input("> Enter registration number:\n> ")
            exp = (r'(^[A-Z]{2}[0-9]{2}\s?[A-Z]{3}$)|(^[A-Z][0-9]{1,3}[A-Z]{3}$)|(^[A-Z]{3}[0-9]{1,3}[A-Z]$)|'
                   r'(^[0-9]{1,4}[A-Z]{1,2}$)|(^[0-9]{1,3}[A-Z]{1,3}$)|(^[A-Z]{1,2}[0-9]{1,4}$)|'
                   r'(^[A-Z]{1,3}[0-9]{1,3}$)|(^[A-Z]{1,3}[0-9]{1,4}$)|(^[0-9]{3}[DX]{1}[0-9]{3}$)')
            if input_reg.upper() == 'Q':
                raise ReturnToMenu  # cancels and returns to menu
            elif re.search(exp, input_reg.upper()) is None:
                print('Invalid registration entered, please try again.')
            else:
                reg = input_reg
        return reg

    @staticmethod
    def input_manufacturer():
        manufacturer = None
        while manufacturer is None:
            input_manufacturer = input("> Enter manufacturer:\n> ")
            if input_manufacturer.upper() == 'Q':
                raise ReturnToMenu  # cancels and returns to menu
            elif input_manufacturer.upper() in ['CHEVROLET', 'CHRYSLER', 'FORD', 'HONDA', 'ISUZU', 'TOYOTA']:
                manufacturer = input_manufacturer
            else:
                print('Invalid manufacturer entered, please try again.')
        return manufacturer

    @staticmethod
    def input_model():
        model = None
        while model is None:
            input_model = input("> Enter model:\n> ")
            if input_model.upper() == 'Q':
                raise ReturnToMenu  # cancels and returns to menu
            else:
                model = input_model
        return model

    @staticmethod
    def input_sipp():
        sipp = None
        while sipp is None:
            input_sipp = input("> Enter SIPP code:\n> ")
            exp = r'^[CDEFGHIJOPRSU][BCDFKLPQTVW][ABCDNM][CDEHINQRVZ]$'
            if input_sipp.upper() == 'Q':
                raise ReturnToMenu  # cancels and returns to menu
            elif re.search(exp, input_sipp.upper()) is None:
                print('Invalid SIPP code entered, please try again.')
            else:
                sipp = input_sipp
        return sipp

    @staticmethod
    def input_seating_capacity():
        seating_capacity = None
        while seating_capacity is None:
            input_seating_capacity = input("> Enter seating capacity:\n> ")
            if input_seating_capacity.upper() == 'Q':
                raise ReturnToMenu  # cancels and returns to menu
            elif input_seating_capacity.isdigit() and 1 < int(input_seating_capacity) <= 10:
                seating_capacity = input_seating_capacity
            else:
                print("Invalid number of seats entered, please try again.")
        return seating_capacity

    @staticmethod
    def input_width():
        width = None
        while width is None:
            input_width = input("> Enter width:\n> ")
            if input_width.upper() == 'Q':
                raise ReturnToMenu  # cancels and returns to menu
            elif input_width.isdigit() and 1000 <= int(input_width) <= 2500:
                width = input_width
            else:
                print("Invalid width entered, please try again.")
        return width

    @staticmethod
    def input_length():
        length = None
        while length is None:
            input_length = input("> Enter length:\n> ")
            if input_length.upper() == 'Q':
                raise ReturnToMenu  # cancels and returns to menu
            elif input_length.isdigit() and 1000 <= int(input_length) <= 10000:
                length = input_length
            else:
                print("Invalid length entered, please try again.")
        return length

    @staticmethod
    def input_speed():
        max_speed = None
        while max_speed is None:
            input_max_speed = input("> Enter maximum speed:\n> ")
            if input_max_speed.upper() == 'Q':
                raise ReturnToMenu  # cancels and returns to menu
            elif input_max_speed.isdigit() and int(input_max_speed) > 0:
                max_speed = input_max_speed
            else:
                print("Invalid speed entered, please try again.")
        return max_speed

    @staticmethod
    def input_mpg():
        mpg = None
        while mpg is None:
            input_mpg = input("> Enter the vehicle's range (mpg):\n> ")
            if input_mpg.upper() == 'Q':
                raise ReturnToMenu  # cancels and returns to menu
            elif input_mpg.isdigit() and int(input_mpg) > 0:
                mpg = input_mpg
            else:
                print("Invalid range (mpg) entered, please try again.")
        return mpg

    def ui_remove_car(self):
        d_yes_or_no = False
        car_item = self.get_car_from_pos()
        while d_yes_or_no is False:  # validates that answer is y or n
            self.display_header()
            print(f'{str(car_item[1]).rjust(3)}  {Car.__str__(self=car_item[0])}')
            print("Remove car? (y/n)")
            ans = input("> ")
            ans = ans.upper()
            if ans == 'Y':
                self.my_car_registry.remove_car(car_to_remove=car_item[0])  # removes car
                d_yes_or_no = True
            elif ans == 'N':
                d_yes_or_no = True
            else:
                print('Please enter \'y\' or \'n\'!')  # error message
        raise ReturnToMenu

    def ui_hire_out(self):
        car_id = self.get_car_from_pos()[0].car_id
        self.my_car_registry.hire_out(car_id)
        raise ReturnToMenu  # returns to menu

    def ui_return_car(self):
        car_id = self.get_car_from_pos()[0].car_id
        self.my_car_registry.return_car_to_garage(car_id)
        raise ReturnToMenu  # returns to menu

    def get_car_from_pos(self):
        valid_car_id = False
        while valid_car_id is False:
            print("> Enter car position: ")
            car_pos = input("> ")
            if car_pos.isdigit() is True:
                car_pos = int(car_pos)
                if (car_pos - 1) in range(0, len(self.my_car_registry.cars_list)):
                    car_obj = self.my_car_registry.cars_list[car_pos - 1]
                    return car_obj, car_pos
                else:
                    print(f"There is no vehicle in position {car_pos}.")
            else:
                print("Please enter a numeric value.")

    @staticmethod
    def ui_exit():
        correct_input_exit = False
        while not correct_input_exit:
            print("> Would you like to exit? (y/n)")
            exit_y_or_n = input('> ')
            if exit_y_or_n.upper() == 'Y':
                exit()
            elif exit_y_or_n.upper() == 'N':
                correct_input_exit = True
            else:
                print('Please enter \'y\' or \'n\'!')
        raise ReturnToMenu  # returns to menu
