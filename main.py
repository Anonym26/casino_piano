import os
import shutil
from random import randint

# Пользовательские данные (текущий баланс, сумма пополнений, сумма ставок)
user = {'balance': 0, 'dep': 0, 'sum': 0}


# Функция очистки консоли
def clear_console():
    """Очищает консоль от всех символов"""
    os.system('cls' if os.name == 'nt' else 'clear')

# Функция проверки валидности ставки
def valid_bet(x: str) -> bool:
    """Возвращает True если ставка меньше или равна балансу и False если больше"""
    if x.isdigit():
        if user['balance'] >= int(x):
            return True
    return False



#  Главное меню
def main_menu():
    while True:
        clear_console()
        print('{{:-^{}}}'.format(shutil.get_terminal_size().columns).format('Casino Piano'))
        print('Главное меню\n\n 1. Выбрать игру\n 2. Пополнить баланс\n 3. Статистика')
        select_menu_item = input('\n\nВыбирете пункт: ')
        if select_menu_item == '1':
            clear_console()
            choise_game()
        elif select_menu_item == '2':
            clear_console()
            add_dep()
        elif select_menu_item == '3':
            clear_console()
            statistics()
        else:
            print('\nОшибка выбора. Нажмите <Enter> для продолжения.')
            input()


# Меню выбора игры
def choise_game():
    """Выбор игры"""
    while True:
        clear_console()
        print('\nВыбор игры\n\n 1. Рулетка\n 2. Blackjack\n 3. Выход в меню')
        select_menu_item = input('\n\nВыбирете пункт: ')
        if select_menu_item == '1':
            mode_roulette()
        elif select_menu_item == '2':
            print('\n\nИгра еще не готова. Нажмите <Enter> для продолжения.')
            input()
        elif select_menu_item == '3':
            clear_console()
            break
        else:
            print('\n\nОшибка ввода. Нажмите <Enter> для продолжения.')
            input()

# Игра "Рулетка"
# Меню выбора режима игры в "Рулетку"
def mode_roulette():
    while True:
        clear_console()
        print('{{:-^{}}}'.format(shutil.get_terminal_size().columns).format('Рулетка'))
        print('Выберите режим игры\n\n 1. Ставка на число\n 2. Ставка на цвет\n 3. Выход в меню выбора игры')
        select_menu_item = input('\n\nВыбирете пункт: ')
        if select_menu_item == '1':
            pass
        elif select_menu_item == '2':
            pass
        elif select_menu_item == '3':
            clear_console()
            break
        else:
            print('\n\nОшибка ввода. Нажмите <Enter> для продолжения.')
            input()


def roulette_num():
    num_bet = input('\nВыберите число от 0 до 36: ')
    if num_bet.isdigit() and 0 <= int(num_bet) <= 36:
        sum_bet = input('\nВведите сумму ставки: ')
        if sum_bet.isdigit():
            user['balance'] -= int(sum_bet)
            user['sum'] += int(sum_bet)
            result = randint(0, 36)
            if result != int(num_bet):
                print('\nВы проиграли. Ваша ставка: ', num_bet, 'Выпало: ', result,
                      '\n\nДля выхода в меню нажмите Enter')
                input()
            else:
                print('\nВы выйграли! Ваша ставка: ', num_bet, 'Выпало: ', result,
                      '\n\nДля выхода в меню нажмите Enter')
                user['balance'] += int(sum_bet) * 36
                input()
        else:
            print('\n\nОшибка ввода. Для выхода в меню нажмите <Enter>.')
            input()
    else:
        print('\n\nОшибка ввода. Для выхода в меню нажмите <Enter>.')
        input()
def roulette():
    """Игра Рулетка"""
    clear_console()
    print('{{:-^{}}}'.format(shutil.get_terminal_size().columns).format('Рулетка'))
    print('Делайте ваши ставки, господа!\n')
    type_bet = input('Выберите тип ставки (1 - число, 2 - цвет): ')
    if type_bet == '1':
        roulette_num()
        # num_bet = input('\nВыберите число от 0 до 36: ')
        # sum_bet = input('\nВведите сумму ставки: ')
        # user['balance'] -= int(sum_bet)
        # user['sum'] += int(sum_bet)
        # if sum_bet.isdigit():
        #     result = randint(0, 36)
        #     if result != int(num_bet):
        #         print('\nВы проиграли. Ваша ставка: ', num_bet, 'Выпало: ', result,
        #               '\n\nДля выхода в меню нажмите Enter')
        #         input()
        #     else:
        #         print('\nВы выйграли! Ваша ставка: ', num_bet, 'Выпало: ', result,
        #               '\n\nДля выхода в меню нажмите Enter')
        #         user['balance'] += int(sum_bet) * 36
        #         input()

    elif type_bet == '2':
        color_bet = input('\nВыберите цвет ставки (1 - red, 2 - black): ')
        sum_bet = input('Введите сумму ставки: ')
        user['balance'] -= int(sum_bet)
        user['sum'] += int(sum_bet)
        red_num = [1, 14, 9, 18, 7, 12, 3, 32, 19, 21, 25, 34, 27, 36, 30, 23, 5, 16]
        result = randint(0, 36)
        if color_bet == '1':
            if red_num.count(result) > 0:
                print('\nВы выйграли! Ваша ставка: ', color_bet, 'Выпало: ', result, 'red',
                      '\n\n\nДля выхода в меню нажмите Enter')
                user['balance'] += int(sum_bet) * 2
                input()
            elif red_num.count(result) <= 0 or result == '0':
                print('\nВы проиграли. Ваша ставка: ', color_bet, 'Выпало: ', result, 'black',
                      '\n\n\nДля выхода в меню нажмите Enter')
                input()
        elif color_bet == '2':
            if red_num.count(result) <= 0:
                print('\nВы выйграли! Ваша ставка: ', color_bet, 'Выпало: ', result, 'black',
                      '\n\n\nДля выхода в меню нажмите Enter')
                user['balance'] += int(sum_bet) * 2
                input()
            elif red_num.count(result) > 0 or result == '0':
                print('\nВы проиграли. Ваша ставка: ', color_bet, 'Выпало: ', result, 'red',
                      '\n\n\nДля выхода в меню нажмите Enter')
                input()


# Пополнение баланса
def add_dep():
    """Внесение депозита и пополнение баланса"""
    clear_console()
    print("\nПополнение баланса\n")
    dep = input('Введите сумму пополнения: ')
    if dep.isdigit():
        user['balance'] += int(dep)
        user['dep'] += int(dep)
        print('\nБаланс пополнен!', '\nВаш баланс: ', user['balance'], '$',
              '\n\n\nДля выхода в меню нажмите <Enter>')
        input()
    else:
        print('\n\nОшибка ввода. Для выхода в меню нажмите <Enter>.')
        input()


# Статистика
def statistics():
    """"Показывает статистику (текущий баланс, сумму пополнений и сумму ставок)"""
    clear_console()
    print("\nCтатистика")
    print('\n Ваш баланс: ', user['balance'], '$', '\n Cумма пополнения депозита: ', user['dep'], '$',
          '\n Cумма ставок: ', user['sum'], '$', '\n\n\nДля выхода в меню нажмите <Enter>')
    input()




if __name__ == '__main__':
    main_menu()
