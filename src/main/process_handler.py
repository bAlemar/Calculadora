#imports os contructor
from src.view.layout_first_view import introduction_page
from src.main.constructor.layout_first_constructor import layout_first_process
from src.main.constructor.calculadora_1_constructor import calculadora_1_process
from src.main.constructor.calculadora_2_constructor import calculadora_2_process
def start() -> None:
    while True:
        command = layout_first_process()

        if command == '1': calculadora_1_process()
        elif command == '2': calculadora_2_process()
        # elif command == '3': calculadora_3_process()
        else:exit()