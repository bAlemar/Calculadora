from src.controllers.calculadora_1_controller import Calculadora_1
from src.view.calculadora_1_view import Calculadora_1_Views
def calculadora_1_process():
    
    calculadora_1_view = Calculadora_1_Views()
    # enter_number = calculation.random_real_number(1,100)

    real_number = calculadora_1_view.calculadora_1_view()
    calculadora_1_controller = Calculadora_1()
    response = calculadora_1_controller.calculations(real_number)
    
    if response["success"]:
        calculadora_1_view.calculadora_1_success(response["attributes"])
    else:
        calculadora_1_view.calculadora_1_error(response["error"])
    return