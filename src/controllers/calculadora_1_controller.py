import math
from src.fachada.calculation import math_operations
from typing import Dict, List
# Recebe Numero Real
# Divide em 3 partes iguais
# 1 parte divide por 4 depois soma 7. tira raiz quadrada e multiplica por 0.257
# 2 parte eleva potêncai 2.121, divide por 5 e soma 1
# 3 parte não faz nada
# Resultado final: Média dos 3 valores

class Calculadora_1:
    def __init__(self) -> None:
        # Comum calculations
        self.nome = "Calculadora 1"
    
    def calculations(self,number:float) -> Dict:
        try:
            number = float(number)
            
            self.entry_number = number

            self.number = number//3
            
            resultado_1 = self.__calculadora_parte_1(self.number)
            
            resultado_2 = self.__calculadora_parte_2(self.number)

            resultado_3 = self.number
            
            result = math_operations.average([resultado_1,resultado_2,resultado_3])
    
            return self.__format_response(result)
        
        except Exception as e:
            return {"success":False,"error":str(e)}


    def __calculadora_parte_1(number):
        number = (number/4) + 7
        number = math.sqrt(number) * 0.257
        return number
    
    def __calculadora_parte_2(number):
        number = number ** 2.121
        number = (number / 5) + 1
        return number
    
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



# Corrigir e botar esses classes como metódos privados dentro de Calculadora_1()
# Processamento só em um método privado

# Nao vai alterando valor com self. isso da merda
# class Calculadora_1_parte_1:
#     def __init__(self,number) -> None:
#         self.number = number

#     def run(self):
#         self.__parte_1()
#         self.__parte_2()
#         return self.number
    
#     # isso virará variável
#     def __parte_1(self):
#         self.number = (self.number/4) + 7

#     def __parte_2(self):
#         self.number = math.sqrt(self.number) * 0.257


# class Calculadora_1_parte_2:
#     def __init__(self,number) -> None:
#         self.number = number
    
#     def run(self):
#         self.__parte_1()
#         self.__parte_2()
#         return self.number
    
#     def __parte_1(self):
#         self.number = self.number ** 2.121
#     def __parte_2(self):
#         self.number = (self.number/5) + 1

