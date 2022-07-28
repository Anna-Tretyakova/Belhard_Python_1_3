"""
Написать функцию hide_debit_numbers которая скрывает номер платежной карты,
оставляя только первые 4 и последние 4 цифра, а остальные заменяет символом *

Пример:
1111222233334444 -> 1111********4444
"""


def hide_debit_numbers(card_number: str) -> str:
    """Скрывает номер карты, оставляя толdько первые и последние 4 цифры

    :param card_number: номер карты 16 цифр
    :return: номер карты, вида 1111********1111
    """
    str(c_numb)
    result = f"{c_numb[0]} {c_numb[1]} {c_numb[2]} {c_numb[3]} {'********'} {c_numb[12]} {c_numb[13]} {c_numb[14]} {c_numb[15]}"
    return result



if __name__ == '__main__':
    c_numb = input("Введите номер карты 16 цифр: ")
    if len(c_numb) == 16 and c_numb.isdigit():
        print(hide_debit_numbers(c_numb))
    print("Некорректный номер карты")


