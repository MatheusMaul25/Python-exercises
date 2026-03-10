import random

def gen_nine_digits():

    random_nine_digits = ''
    for _ in range(9):
        random_nine_digits += str(random.randint(0, 9))
    return random_nine_digits

def digit_1(nine_digits):

    regressive_counter_1 = 10
    result = 0
    for digit in nine_digits:
        result += int(digit) * regressive_counter_1
        regressive_counter_1 -= 1
    digit_1 = (result * 10) % 11
    return digit_1 if digit_1 <= 9 else 0

def digit_2(ten_digits):

    regressive_counter_2 = 11
    result = 0
    for digit in ten_digits:
        result += int(digit) * regressive_counter_2
        regressive_counter_2 -= 1
    digit_2 = (result * 10) % 11
    return digit_2 if digit_2 <= 9 else 0


def gen_cpf():

    nine_digits = gen_nine_digits()

    result_digit_1 = digit_1(nine_digits)

    ten_digits = nine_digits + str(result_digit_1)

    result_digit_2 = digit_2(ten_digits)

    cpf_generated = f'{nine_digits}{result_digit_1}{result_digit_2}'

    return cpf_generated

def number_of_cpf_number():

    amount = input("Quantos cpf's deseja criar? -> ").strip()

    try:
        amount_int = int(amount)
        if amount_int < 0:
            raise ValueError('Digíte um número maior que zero.')
        for _ in range(amount_int):
            print(gen_cpf())
    except ValueError:
        print('Valor inválido')