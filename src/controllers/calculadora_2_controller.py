from typing import List,Dict
from src.fachada.calculation import math_operations

class Calculadora_2:
    def __init__(self) -> None:
        self.nome = 'Calculadora 2'

    
    def calculations(self,list_numbers:List) -> Dict:
        try:
            self.entry_number = list_numbers

            result = calculo(list_numbers).run()
            
            return self.__format_response(result)
        
        except Exception as e: 
            return {"success":False,"error":str(e)}


    def __format_response(self,result:List) -> Dict:
        # Isso deveria ficar na view?
        return {
            "success":True,
            "attributes":{
                "Tipo_Calculadora":self.nome,
                "Entradas":self.entry_number,
                "Status":"Sucesso",
                "resultado":result,
            }
        }

class calculo:
    def __init__(self,list_numbers:List) -> None:
        self.list_numbers = list_numbers
        self.__fixing_list_number()
    
    def run(self) -> float:
        result = math_operations.standard_deviation(self.list_numbers)
        return 1/result
    
    def __calculo_1(self,number:float) -> float:
        number = number * 11
        number = number**0.95

        return number
    
    def __fixing_list_number(self) -> List:
        self.list_numbers = self.list_numbers.split(',')
        self.list_numbers = [self.__calculo_1(float(x.strip())) for x in self.list_numbers]


        
