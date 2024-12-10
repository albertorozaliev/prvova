
from functools import reduce


admin = {
    "login": "admin",
    "password": "123"
}


user = {
    "login": "Vova",
    "password": "321"
}


korzina = [
    {"название": " "},
]


currencies = [
    {"название": "Доллар", "цена": 75},
    {"название": "Евро", "цена": 85},
    {"название": "Фунт", "цена": 100},
    {"название": "Иена", "цена": 0.7},
    {"название": "Рубль", "цена": 1},
]


currencies = sorted(currencies, key=lambda x: x['цена'])


def display_currencies():
    for currency in currencies:
        print(f"{currency['название']}: {currency['цена']}")



def filter_currencies():
    price_limit = float(input("Введите минимальную цену для фильтрации валют: "))
    filtered = list(filter(lambda x: x['цена'] > price_limit, currencies))
    if filtered:
        for currency in filtered:
            print(f"{currency['название']}: {currency['цена']}")
    else:
        print("Нет валют, соответствующих критериям.")



def buy_currency():
    name = input("Введите название валюты: ")
    korzina.append({"название": name})
    print("Валюта добавлена.")



def sell_currency_korzina():
    display_currencies()
    index = int(input("Введите номер валюты для продажи: ")) - 1
    if 0 <= index < len(korzina):
        korzina.pop(index)
        print("Валюта удалена.")
    else:
        print("Неверный номер валюты.")


def per_currency_korzina():
    print('Введите номер UIT для перевода')
    l = input
    display_currencies()
    index = int(input("Введите номер валюты для перевода: ")) - 1
    if 0 <= index < len(korzina):
        korzina.pop(index)
        print("Валюта переведена.")
    else:
        print("Неверный номер валюты.")



def add_currency():
    name = input("Введите название валюты: ")
    price = float(input("Введите цену валюты: "))
    currencies.append({"название": name, "цена": price})
    print("Валюта добавлена.")


def update_currency():
    print(currencies)
    index = int(input("Введите номер валюты для изменения: ")) - 1
    if 0 <= index < len(currencies):
        name = input("Введите новое название валюты: ")
        price = float(input("Введите новую цену валюты: "))
        currencies[index] = {"название": name, "цена": price}
        print("Данные о валюте обновлены.")
    else:
        print("Неверный номер валюты.")


def delete_currency():
    display_currencies()
    index = int(input("Введите номер валюты для удаления: ")) - 1
    if 0 <= index < len(currencies):
        currencies.pop(index)
        print("Валюта удалена.")
    else:
        print("Неверный номер валюты.")


main = 1
while main == 1:
    while True:
        try:
            print('Добро пожаловать на биржу BYBIT')
            print('Выберите от какого имени вы будете использовать биржу: 1.админ. 2.пользователь.')
            a = int(input())

            if a < 1 or a > 2:
                print("Вы ввели не ту цифру, необходимо выбрать 1 или 2")
            else:
                if a == 1:
                    print(f"Ваш выбор: admin")
                    main = 0
                elif a == 2:
                    print(f"Ваш выбор: пользователь")
                    main = 0
        except ValueError:
            print("Вы должны ввести число")
            main = 0
            break


        if a == 1:
            print('Ведите логин администратора биржы')
            b = input()
            try:
                if b == admin['login']:
                    print('Ведите пароль администратора биржы')
                    c = input()
                else:
                    print(" ")
            except ValueError:
                print("Вы ввели неправльный логин")
                main = 0
                break


            try:
                if c == admin['password']:
                    print('Добро пожаловать на биржу, администратор')
                    while True:
                        print('Что вы хотите сделать?')
                        print('1.Показать валюты')
                        print('2.Добавить валюту')
                        print('3.Изменить валюту')
                        print('4.Удалить валюту')
                        print('5.Фильтровать валюты по цене')
                        print('6.Выйти')
                        d = input()
                        if d == '1':
                            display_currencies()
                        elif d == '2':
                            add_currency()
                        elif d == '3':
                            update_currency()
                        elif d == '4':
                            delete_currency()
                        elif d == '5':
                            filter_currencies()
                        elif d == '6':
                            main = 0
                            break
                        else:
                            print("Неверный выбор.")
                else:
                    print('Вы ввели неправильный пароль')
                    main = 0
                    break
            except ValueError:
                print("Вы ввели не то")
                main = 0
                break


        elif a == 2:
            print('Ведите логин')
            b = input()
            try:
                if b == user['login']:
                    print('Ведите пароль биржы')
                    c = input()
                else:
                    print(" ")
            except ValueError:
                print("Вы ввели неправльный логин")
                main = 0
                break


            try:
                if c == user['password']:
                    print('Добро пожаловать на биржу')
                    while True:
                        print('Что вы хотите сделать?')
                        print('1.Купить валюту')
                        print('2.Продать валюту')
                        print('3.Перевести')
                        print('4.Выйти')
                        print('5.Просмотр валюты')
                        print('6.Показать корзину')
                        d = input()
                        if d == '1':
                            buy_currency()
                        elif d == '2':
                            sell_currency_korzina()
                        elif d == '3':
                            per_currency_korzina()
                        elif d == '4':
                            main = 0
                            break
                        elif d == '5':
                            display_currencies()
                        elif d == '6':
                            display_currencies()
                        else:
                            print("Неверный выбор.")
                else:
                    print('Вы ввели неправильный пароль')
                    main = 0
                    break
            except ValueError:
                print("Вы ввели не то")
                main = 0
                break
