
from typing import Dict,List
import os

class Calculadora_3_Views:
    def calculadora_3_view(self) -> str:
        message = """
        Insira uma lista de N números reais, separados por ,
        """
        list_numbers = input('Lista: ')

        return list_numbers
 
    def calculadora_3_success(self,response:Dict) -> None:
        self.__clear()
        message = f"""
        Cálculo feito com Sucesso!!!
        Seus parâmetros são:
        
        Tipo Calculadora: {response["Tipo_Calculadora"]}
        Entradas: {response["Entradas"]}
        Variancia: {round(response["Variancia"],2)}
        Desvio Padrão: {round(response["Std"],2)}
        Status: {response["Status"]}
        Resultado: {response["resultado"]}
        """

        print(message)

        return


    def calculadora_3_error(self,error:str) -> None:
        self.__clear()
        message = f"""
        Não foi possivel realizar esse cálculo.
        Error: {error}
        """
        print(message)

        return

    def __clear(self):
        os.system('cls||clear')