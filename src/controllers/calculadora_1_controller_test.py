from src.controllers.calculadora_1_controller import Calculadora_1
# from src.controllers.calculadora_1_controller import Calculadora_1
from faker import Faker


fake = Faker()


def test_calculadora_1():
    number1 = fake.random_number()
    calculadora_1 = Calculadora_1(number1)
    
    expect = True

    result = calculadora_1.calculations()["success"]

    assert expect == result


