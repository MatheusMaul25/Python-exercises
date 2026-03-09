import os
import sys
items_list = []

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_items_list():
    for indice, item in enumerate(items_list, start=1):
        print(f'{indice}- {item}')

def insert_item():
    value = input('Item: ').upper()
    if value not in items_list:
        items_list.append(value)
    else:
        print('Item já está na lista')

def delete_item():
    show_items_list()
    value = input('Escolha um índice para apagar: ')
    try:
        int_valor = int(value)
        del items_list[int_valor - 1]
        clear()
    except ValueError:
        print('Digite um número inteiro')
    except IndexError: 
        print('Esse índice não é válido!!')
    except Exception:
        print('ERRO inesperado!')

def list_items():
    if not items_list:
        print('Nada para listar!')
    else:
        show_items_list()

def invalid_option():
    print('Por favor, escolha uma opção válida (i, a, l).')

def exit_program():
    print('Encerrando programa...')
    sys.exit()