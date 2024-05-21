from faker import Faker
from src.controllers.calculadora_1_controller import Calculadora_1


fake = Faker()


def test_calculadora_1():
    number1 = fake.random_number()
    calculadora_1 = Calculadora_1()
    
    expect = True

    result = calculadora_1.calculations(number1)["success"]

    assert expect == result


