from faker import Faker
from src.controllers.calculadora_2_controller import Calculadora_2


fake = Faker()


def test_calculadora_2():
    random_list_numbers = [fake.random_int() for _ in range(fake.random_int())]
    random_list_numbers = str(random_list_numbers)[1:-1]
    calculadora_2 = Calculadora_2()
    
    expect = True

    response = calculadora_2.calculations(random_list_numbers)
    result = response['success']
    assert expect == result


