from faker import Faker
from src.controllers.calculadora_3_controller import Calculadora_3


fake = Faker()


def test_calculadora_3():
    random_list_numbers = [fake.random_int() for _ in range(fake.random_int())]
    random_list_numbers = str(random_list_numbers)[1:-1]
    calculadora_3 = Calculadora_3()
    
    expect = True

    response = calculadora_3.calculations(random_list_numbers)
    result = response['success']
    assert expect == result


