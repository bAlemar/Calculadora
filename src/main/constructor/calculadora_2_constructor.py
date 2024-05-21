from src.view.calculadora_2_view import Calculadora_2_Views
from src.controllers.calculadora_2_controller import  Calculadora_2



def calculadora_2_process():
    view = Calculadora_2_Views()
    controller = Calculadora_2()
    
    list_numbers = view.calculadora_2_view()
    response = controller.calculations(list_numbers)

    if response["success"]:
        view.calculadora_2_success(response["attributes"])
    else:
        view.calculadora_2_error(response["error"])