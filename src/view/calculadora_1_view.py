from typing import Dict
import os

#    "Tipo_Calculadora":self.nome,
                # "Entradas":self.entry_number,
                # "Status":"Sucesso",
                # "resultado":result,
class Calculadora_1_Views:
    def calculadora_1_success(self,response:Dict):
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


    def calculadora_1_error(self,response:Dict):
        self.__clear()
        message = f"""
        Não foi possivel realizar esse cálculo.
        Error: {response["error"]}
        """

        print(message)

        return

    def __clear(self):
        os.system('cls||clear')