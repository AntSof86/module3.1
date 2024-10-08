# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
# строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
# v1. Создать переменную calls = 0 вне функций.
# v2. Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных
# двух функциях.
# v3. Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# v4. Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# v5. Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# v6. Вывести значение переменной calls на экран(в консоль).

calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    stroka = str(string)
    result = (len(stroka), stroka.upper(), stroka.lower())
    count_calls()
    return result

def is_contains(string, list_to_search):    # 4
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
