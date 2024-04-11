from Classes.ui import Ui
import os


def main():
    my_ui = Ui()
    while my_ui.return_to_menu is True:
        os.system('cls')
        my_ui.display_header()
        my_ui.display_items()
        my_ui.display_menu()
        my_ui.process_option()


if __name__ == "__main__":
    main()
