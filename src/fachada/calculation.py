import numpy as np
from typing import List

class __Calculation:
    def __init__(self) -> None:
        self.__np = np

    def random_real_number(self,number_min:int,number_max:int) -> int:
        """
        Escolhe número aleatório entre os range max e min
        number_min: Range Mínimo do Número
        number_max: Range Máximo do Número
        """
        random_number = self.__np.random.randint(number_min,number_max)
        return random_number

    def average(self,numbers:List) -> float:
        average_number = self.__np.average(numbers)
        return average_number

    def standard_deviation(self,numbers:List):
        sd_number = self.__np.std(numbers)
        return sd_number

    
math_operations = __Calculation()