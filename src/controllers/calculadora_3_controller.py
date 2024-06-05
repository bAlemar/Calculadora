from typing import List, Dict, Tuple
from src.fachada.calculation import math_operations

class Calculadora_3:
    def __init__(self) -> None:
        self.nome = "Calculadora 3"
   
    def calculations(self,list_numbers:List) -> Dict:
        try:
            self.entry_number = list_numbers
            variance,standard_deviation = self.__calculo(self.entry_number)
            result = self.__compare_variance_std(variance,standard_deviation)
            self.variance = variance
            self.std = standard_deviation
            return self.__format_response(result)
        except Exception as e: 
            return {"success":False,"error":str(e)}
    
    def __compare_variance_std(self,variance,standard_deviation):
        if variance > standard_deviation:
            return "Varianca Maior"
        else:
            return "Varianca Menor"
    
    def __calculo(self,list_numbers) -> Tuple[float,float]:
        list_numbers = self.__fixing_list_number(list_numbers)
        variance  =  math_operations.variance(list_numbers)
        standard_deviation = math_operations.standard_deviation(list_numbers)
        return [variance,standard_deviation]

    def __fixing_list_number(self,list_numbers) -> List:
        list_numbers = list_numbers.split(',')
        list_numbers = [float(x.strip()) for x in list_numbers]
        return list_numbers

    def __format_response(self,result:List) -> Dict:
        # Isso deveria ficar na view?
        return {
            "success":True,
            "attributes":{
                "Tipo_Calculadora":self.nome,
                "Entradas":self.entry_number,
                "Status":"Sucesso",
                "Variancia":self.variance,
                "Std": self.std,
                "resultado":result,
            }
        }


# Método público tipo constructor e lógica no método privado...
# Deixar como métodos privados
# class calculo:
#     def __init__(self,list_numbers:List) -> None:
#         self.list_numbers = list_numbers
#         self.__fixing_list_number()
#     def run(self):
#         return self.__calculo_1()
#     def __calculo_1(self) -> Tuple[float,float]:
#         variance  =  math_operations.variance(self.list_numbers)
#         standard_deviation = math_operations.standard_deviation(self.list_numbers)
#         return [variance,standard_deviation]
#     def __fixing_list_number(self) -> List:
#         self.list_numbers = self.list_numbers.split(',')
#         self.list_numbers = [float(x.strip()) for x in self.list_numbers]
