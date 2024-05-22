from src.controllers.calculadora_3_controller import  Calculadora_3
from src.view.calculadora_3_view import Calculadora_3_Views

def calculadora_3_process():
    view = Calculadora_3_Views()
    controller = Calculadora_3()

    list_numbers = view.calculadora_3_view()
    response = controller.calculations(list_numbers)

    if response["success"]:
        view.calculadora_3_success(response["attributes"])
    else:
        view.calculadora_3_error(response["error"])
    return