# LISTA DE COMPRAS #
from shop_list_package import func_module
menu_options = {'i': func_module.insert_item,
                'a': func_module.delete_item,
                'l': func_module.list_items,
                's': func_module.exit_program }
while True:
    print('selecione uma opção: ')
    user_option = input('[i]Inserir  [a]Apagar  [l]Listar [s]Sair: ').strip().lower()
    func_module.clear()
    action = menu_options.get(user_option, func_module.invalid_option)
    if action:
        action()
