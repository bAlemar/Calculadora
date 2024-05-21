
from typing import Dict,List
import os

class Calculadora_2_Views:
    def calculadora_2_view(self):
        message = """
        Insira uma lista de N números reais, separados por ,
        """
        
        print(message)
        list_numbers = input('Lista: ')
        return list_numbers
 
    def calculadora_2_success(self,response:Dict):
        self.__clear()
        message = f"""
        Cálculo feito com Sucesso!!!
        Seus parâmetros são:
        
        Tipo Calculadora: {response["Tipo_Calculadora"]}
        Entradas: {response["Entradas"]}
        Status: {response["Status"]}
        Resultado: {round(response["resultado"],2)}
        """

        print(message)

        return


    def calculadora_2_error(self,error:str):
        self.__clear()
        message = f"""
        Não foi possivel realizar esse cálculo.
        Error: {error}
        """

        print(message)

        return

    def __clear(self):
        os.system('cls||clear')